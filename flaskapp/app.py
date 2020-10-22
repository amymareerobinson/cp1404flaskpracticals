"""
CP1404 2020 - Practical 10
Student Name: Amy Robinson
Program - App
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f'Hello {name}'


def celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


@app.route('/convert_celsius_to_fahrenheit/<celsius>')
def f(celsius=''):
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    return f'Celsius: {celsius} -to- Fahrenheit: {fahrenheit}'


if __name__ == '__main__':
    app.run()
