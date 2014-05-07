from .base import simple_instruction


@simple_instruction
def concat(first: 'str', second: 'str'):
    return first + second


@simple_instruction
def length(s: 'str'):
    return len(s)


@simple_instruction
def to_int(s: 'str'):
    '''
    If can't parse to integer, is no-op.
    '''
    try:
        return int(s)
    except ValueError:
        return


@simple_instruction
def reverse(s: 'str'):
    return s[::-1]


@simple_instruction(multiple_return_items=True)
def to_chars(s: 'str'):
    return s


@simple_instruction
def contained(first: 'str', second: 'str'):
    return first in second
