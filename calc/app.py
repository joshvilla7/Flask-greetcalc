from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    """Operation that adds a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = add(a, b)
    
    return str(total)


@app.route('/sub')
def subtraction():
    """Operation that subtracts b from a"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = sub(a, b)

    return str(total)


@app.route('/mult')
def multiply():
    """Operation that multiplies a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = mult(a, b)

    return str(total)


@app.route('/div')
def divide():
    """Operation that divides a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = div(a, b)

    return total


"""Single route to consolidate all operations into one function"""

OPERATIONS = {
    "add" : add,
    "sub" : sub,
    "mult": mult,
    "div" : div
}

@app.route('/math/<operate>')
def math(operate):
    """Operation that combines all operations"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = OPERATIONS[operate](a, b)

    return str(total)
