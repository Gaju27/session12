import math

# cos_call.py
from Calculator.decorator import fstring_print

__all__ = ['cos_']


@fstring_print
def cos_(value):
    """Calculate cos(value)"""
    return math.cos(value)


@fstring_print
def cos_d(value):
    """Derivative of cos(x) is negative sin(x)"""
    return - math.sin(value)
