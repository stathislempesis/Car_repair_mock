import json
from datetime import datetime

# import flask dependencies
from flask import Flask, make_response, jsonify, request

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    
    parameters = req.get('queryResult').get('parameters')
    
    not_available_dates = [datetime(2019, 3,26), datetime(2019, 3, 27)]
    
    if parameters['car-type'] and parameters['service-option'] and parameters['date']:
       selected_date = datetime.strptime(parameters['date'].split('T')[0], '%Y-%m-%d')
       
       if(parameters['date'] in not_available_dates):
            response = make_response(jsonify({'fulfillmentText': 'There is not free slot at your selected date. Please choose another day.'}))
       else:
            response = make_response(jsonify({'fulfillmentText': 'You are all booked.'}))
    else:
       response = make_response(jsonify({'fulfillmentText': 'Something else.'}))
        
    # return a fulfillment response
    return response

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def hello():
    return results()

# run the app
if __name__ == '__main__':
   app.run()
