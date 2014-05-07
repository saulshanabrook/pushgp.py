from .base import simple_instruction


@simple_instruction
def and_(first: 'bool', second: 'bool'):
    return first and second


@simple_instruction
def or_(first: 'bool', second: 'bool'):
    return first or second


@simple_instruction
def not_(b: 'bool'):
    return not b


@simple_instruction
def xor(first: 'bool', second: 'bool'):
    return first != second


@simple_instruction
def from_int(i: 'int'):
    return bool(i)


@simple_instruction
def from_float(f: 'float'):
    return bool(f)
