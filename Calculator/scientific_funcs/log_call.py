import math

from Calculator.decorator import fstring_print

__all__ = ['log_']

@fstring_print
def log_(value):
    """
    :param value: input value must be int or float
    :return: return the log of input value
    """

    if not isinstance(value, (int, float)) or value == 0:
        raise (ValueError, 'Make sure value must be int or float and not zero')
    return math.log(value)


@fstring_print
def log_d(value):
    """
    :param value: input value must be int or float
    :return: return the derivative log of input value
    """
    if not isinstance(value, (int, float)) or value == 0:
        raise (ValueError, 'Make sure value must be int or float and not zero')
    return 1 / value
