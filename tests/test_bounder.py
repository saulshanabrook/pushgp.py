import pytest

from pushgp import bounders


class TestArbitraryBounder(object):

    def test_subset_works(self):
        b = bounders.ArbitraryBounder([1, 2])
        assert b([1], {}) == [1]
        assert b([1, 2, 1], {}) == [1, 2, 1]

    def test_not_subset_raises_error(self):
        b = bounders.ArbitraryBounder([1, 2])
        with pytest.raises(AssertionError):
            b([3], {})
        with pytest.raises(AssertionError):
            b([3, 1, 2], {})
