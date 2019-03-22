# import flask dependencies
from flask import Flask
from flask_ngrok import run_with_ngrok

# initialize the flask app
app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

# default route
@app.route('/')
def index():
    return 'Hello World!'

# create a route for webhook
@app.route('/webhook')
def hello():
    return 'Hello World!'

# run the app
if __name__ == '__main__':
   app.run()
