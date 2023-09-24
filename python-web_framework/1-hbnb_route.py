# Import the class Flask from flask module
from flask import Flask

# Create an instance of Flask class
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
    A function that returns a text

    return: a text
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
    A function that returns a text

    return: a text
    '''
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')