from .base import simple_instruction


@simple_instruction
def add(first: 'float', second: 'float'):
    return first + second


@simple_instruction
def sub(first: 'float', second: 'float'):
    return first - second


@simple_instruction
def mult(first: 'float', second: 'float'):
    return first * second


@simple_instruction
def div(first: 'float', second: 'float'):
    try:
        return first / second
    except ZeroDivisionError:
        return
