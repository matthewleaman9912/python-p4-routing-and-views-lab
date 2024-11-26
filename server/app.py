#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:number>')
def count(number):
    numbers = list(range(0, number, 1))
    return '\n'.join([str(num) for num in numbers])+'\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '*':
        number = num1 * num2
        return str(number)
    elif operation == '+':
        number = num1 + num2
        return str(number)
    elif operation == '-':
        number = num1 - num2
        return str(number)
    elif operation == 'div':
        number = (num1 / num2)
        return str(number)
    elif operation == '%':
        number = num1 % num2
        return str(number)
    else:
        return None
    