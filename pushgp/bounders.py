class ArbitraryBounder(object):
    """Defines a basic bounding function for lists of values.

    This callable class acts as a function that bounds a
    list to a set of legitimate values. It does this by
    simply verifying that the candidate values are within
    the list of legitimate values.

    For instance, if ``["hey", "hi",]`` was used as the *values* parameter,
    then the candidate ``["what?"]`` would raise an ``AssertionError`` because
    ``what?`` is not in the original values list.

    However if it was called with ``["hi", "hi", "hey"]`` it wouldn't raise an
    error and it would return ``["hi", "hi", "hey"]``.
    Public Attributes:

    - *values* -- the set of attainable values
    """

    def __init__(self, values):
        self.values = set(values)

    def __call__(self, candidate, args):
        assert set(candidate).issubset(self.values)
        return candidate
