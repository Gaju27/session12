import math

from Calculator.decorator import fstring_print

__all__ = ['sigmoid_']

@fstring_print
def sigmoid_(value):
    return 1 / (1 + math.exp(-value))

@fstring_print
def sigmoid_d(value):
    '''f(x) * (1 - f(x))'''
    return sigmoid_(value) * (1-sigmoid_(value))