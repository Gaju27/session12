import math
from collections.abc import Iterable

from Calculator.decorator import fstring_print

__all__ = ['softmax_']


@fstring_print
def softmax_(value: "any") -> float:
    """Compute softmax values for each sets of scores in value."""
    if not (all(isinstance(i, (int, float)) for i in value) and isinstance(value, Iterable)):
        raise Exception('Make sure value must be int or float and iterable too')
    return 1 / (1 + math.exp(-value))


# @fstring_print
# def softmax_d_(value):
#     """Compute Derivative of softmax."""
#     if not (all(isinstance(i, (int, float)) for i in value) and isinstance(value, Iterable)):
#         raise Exception('Make sure value must be int or float and iterable too')
#     # Reshape the 1-d softmax to 2-d so that np.dot will do the matrix multiplication
#     s = value.reshape(-1, 1)
#     return np.diagflat(s) - np.dot(s, s.T)
#
#
# x = softmax_([1, 2, 3])
# softmax_d_(x)
