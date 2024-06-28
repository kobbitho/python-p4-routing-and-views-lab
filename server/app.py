#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:hello>')
def print_string(hello):
    print(hello)
    return 'hello'

@app.route('/count/<int:parameter>')
def count (parameter):
    count = f''
    for param in range(parameter):
        count += f'{param}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return str(result)    
 
if __name__ == '__main__':
    app.run(port=5555, debug=True)   
