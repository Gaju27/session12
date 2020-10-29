from Calculator.decorator import fstring_print

__all__ = ['relu_']


@fstring_print
def relu_(value):
    """
   :param value: input list of value for the calculation for relu
   :return: return relu value which is 0 to value
    """
    if not isinstance(value, (int, float)):
        raise (ValueError, 'Make sure value must be int,float')
    return 1  if value > 0 else 0


@fstring_print
def relu_d(value):
    """
    :param value: input value for the derivative calculation for relu
    :return: return the derivative of relu
    """
    if not isinstance(value, (int, float)):
        raise (ValueError, 'Make sure value must be int,float')
    return 0 if value > 0 else 0

