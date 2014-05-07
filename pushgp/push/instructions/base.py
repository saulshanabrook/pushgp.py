from functools import wraps
from inspect import signature

from . import utils


@utils.optional_arguments
def simple_instruction(f, multiple_return_items=False):
    '''
    Wraps an instruction funtion ``f`` to have it take its arguments from
    Push stacks and add the return value to the ``exec``.

    It requires that the function arguments be annotated with the stacks that
    they draw from. If the stacks don't have enough values on them, it will
    not modify anything.

    If ``multiple_return_items`` is True, than will assume the function returns
    an iterable of items, instead of only one item. It will push each
    indivually to the ``exec``, instead of pushing the iterable as one
    item.
    '''
    @wraps(f)
    def wrapper(Push):
        kwargs = {}
        for parameter in signature(f).parameters.values():
            try:
                kwargs[parameter.name] = Push[parameter.annotation].pop()
            except IndexError:
                return
        return_item = f(**kwargs)
        if return_item is not None:
            if multiple_return_items:
                Push['exec'].extend(return_item)
            else:
                Push['exec'].append(return_item)
    return wrapper
