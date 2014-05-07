'''
from https://wiki.python.org/moin/PythonDecoratorLibrary#Creating_decorator_with_optional_arguments
'''
import functools
import inspect


def optional_arguments(fn):
    ''' Allow to use decorator either with arguments or not. '''

    def wrapped_decorator(*args, **kwargs):
        if len(args) == 1 and callable(args[0]) and not kwargs:
            return fn(args[0])
        else:
            def real_decorator(decoratee):
                return fn(decoratee, *args, **kwargs)

            return real_decorator

    return wrapped_decorator
