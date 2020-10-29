import math

# Sin_call.py
from Calculator.decorator import fstring_print

__all__ = ['sin_']


@fstring_print
def sin_(value):
    '''Calculate sin(value)'''
    return math.sin(value)


@fstring_print
def sin_d(value):
    '''Derivative of sin(x) is cos(x)'''
    return math.cos(value)
