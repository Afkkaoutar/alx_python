#!/usr/bin/python3
""" starts a Flask web application and displays 'Hello HBNB', 'HBNB', 'C with thee value of text','n is a number' only if n is an integer and HTML page only if n is integer """

from flask import Flask, render_template
app = Flask(__name__)

# this route is called by default when you run it


@app.route("/", strict_slashes=False)
def display():
    # displays message fto the user
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def show_message():
    # display HBNB message to the user
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def show_C(text):
    # display C with text to the user
    return("C {}".fromat(text.replace("_", " ")))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):
    return("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    # display int number with text to the user
    return("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def show_number_template(n):
    # display in number using temlate
    return(render_template('5-number.html', number=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def show_number_template_even_or_odd(n):
    return(render_template('6-number_odd_or_even.html', number=n))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)