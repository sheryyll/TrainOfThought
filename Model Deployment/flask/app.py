from flask import Flask

''' 
it creates instance of Flask class, 
which will be our WSGI application
'''

# WSGI application
app = Flask(__name__) 

# basic route
@app.route('/')
def welcome():
    return "Welcome to this Flask app!. This must be amazing journey!"

@app.route('/index')
def index():
    return "This is index page of Flask app"


if __name__ == '__main__':
    app.run(debug=True)
