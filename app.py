# import flask dependencies
from flask import Flask

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# create a route for webhook
@app.route('/webhook')
def hello():
    return {'fulfillmentText': 'This is a response from webhook.'}

# run the app
if __name__ == '__main__':
   app.run()
