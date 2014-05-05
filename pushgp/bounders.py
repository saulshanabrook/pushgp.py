class LengthBounder(object):
    """Defines a basic bounding function for lists of values under a certain
    length.

    This callable class acts as a function that bounds a
    list to a set of legitimate values. It does this by
    verifying that the candidate values are within the list of legitimate
    values.

    Also, if the length of the list is greater than the ``size_limit``,
    it will return a truncated version of the list, dropping the last elements.

    Public Attributes:

    - *values* -- the set of attainable values
    - *size_limit* -- the max length of the candidate list

    >>> LengthBounder([1, 2], None)([1, 2, 1, 2], {})
    [1, 2, 1, 2]
    >>> LengthBounder([1, 2], None)([1, 1], {})
    [1, 1]
    >>> LengthBounder([1, 2], 2)([1, 2, 1, 2], {})
    [1, 2]
    >>> LengthBounder([1, 2], 3)([1, 2, 1, 2], {})
    [1, 2, 1]
    >>> import pytest
    >>> assert pytest.raises(AssertionError, LengthBounder([1], None), [3], {})
    """

    def __init__(self, values, size_limit):
        self.values = values
        self.size_limit = size_limit

    def __call__(self, candidate, args):
        assert set(candidate).issubset(set(self.values))
        if self.size_limit:
            return candidate[:self.size_limit]
        return candidate
