import math

from Calculator.decorator import fstring_print

__all__=['tan_','tan_h']

@fstring_print
def tan_(value):
    '''calculate the tan of value'''
    return math.tan(value)

@fstring_print
def tan_h(value):
    '''The hyperbolic tangent function is also one-to-one and invertible; its inverse, tanh−1x, is shown in green. It is defined only for −1x1.'''
    return math.tanh(value)


@fstring_print
def tand_(value):
    '''Derivative of tan(x) is 1/cos(x) * cos(x)'''
    return (1/(math.cos(value)**2))

@fstring_print
def tan_hd(value):
    '''Derivative of tanh(x) is 1-tanh(x) * tanh(x)'''
    return 1-(math.tanh(value) ** 2)