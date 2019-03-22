import json

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
    print(parameters['car-type'];)
    #if(action=="hours"):
       # response = make_response(jsonify({'fulfillmentText': 'Our opening hours are Monday - Friday from 9.00 am to 5.00 pm.'}))
    #elif(action=="repair"):
        #response = make_response(jsonify({'fulfillmentText': 'Repair.'}))
    #else:
        #response = make_response(jsonify({'fulfillmentText': 'Something else.'}))
        
    # return a fulfillment response
    return make_response(jsonify({'fulfillmentText': 'Yolo.'})

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def hello():
    return results()

# run the app
if __name__ == '__main__':
   app.run()
