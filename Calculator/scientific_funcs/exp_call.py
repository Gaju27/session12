import math

from Calculator.decorator import fstring_print

__all__ = ['exponential']


@fstring_print
def exponential(value):
    """
       :param value: input value must be int or float
       :return: return the exponential of input value
    """
    return math.exp(value)


@fstring_print
def exponential_d(value):
    """
       :param value: input value must be int or float
       :return: return the derivative exponential of input value
       """
    return exponential(value)
