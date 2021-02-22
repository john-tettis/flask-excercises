from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    b = int(request.args.get('b'))
    a = int(request.args.get('a'))
    result = add(a,b)
    return str(result) 

@app.route('/sub')
def subtraction():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result) 

@app.route('/mult')
def multiplication():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result) 

# part 2

oper ={
    'add':add,
    'sub':sub,
    'mult':mult,
    'div':div,
}

@app.route('/math/<operand>')
def math_route(operand):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = oper[operand](a,b)
    return str(res)