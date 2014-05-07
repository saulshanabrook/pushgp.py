import numbers
import collections
import logging


logger = logging.getLogger(__name__)


class Push(collections.defaultdict):
    '''
    Push interpreter.
    '''

    def __init__(self):
        self.default_factory = list

        self.stack_types = collections.OrderedDict([
            [bool, 'bool'],
            [str, 'str'],
            [numbers.Integral, 'int'],
            [numbers.Real, 'float'],
        ])

    def __str__(self):
        return 'Push: {}'.format(dict(self.items()))

    def __repr__(self):
        return 'Push({}): {}'.format(self.stack_types, dict(self.items()))

    def stack_for_item(self, item):
        '''
        Returns the right stack name for any ``item``, using the
        ``stack_types`` map attribute. If no stack has this type,
        it will return None.
        '''
        for item_type, stack_name in self.stack_types.items():
            if isinstance(item, item_type):
                return stack_name

    def execute(self):
        '''
        Pops each item off the ``exec`` stack until it is empty,
        using the `.pop()` method.

        If the item is in instance in the ``stack_types`` attribute then
        it will be pushed to the corresponding stack.

        Else if it a callable is will be called with the Push object and should
        return a modified Push object.

        Else it will raise a ``TypeError``
        '''

        while self['exec']:
            logger.debug('Starting execution: %s', self)
            item = self['exec'].pop()
            literal_stack_name = self.stack_for_item(item)
            if literal_stack_name:
                self[literal_stack_name].append(item)
            elif callable(item):
                item(self)
            else:
                raise TypeError(
                    '{}:{} is not recognized by Push'.format(type(item), item)
                )
            logger.debug('Finished execution: %s', self)

    def __call__(self, *items):
        '''
        Pushes a list of ``items`` onto the ``exec`` stack and executes them.
        Uses the ._execute() method to run through the ``exec`` stack.
        '''
        logger.debug('Pushing %s', items)

        self['exec'].extend(items)
        self.execute()
        return self
