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
    
    print(action)
    
    # return a fulfillment response
    return make_response(jsonify({'fulfillmentText': 'This is a response from webhook.'}))

# create a route for webhook
@app.route('/webhook')
def hello():
    return results()

# run the app
if __name__ == '__main__':
   app.run()
