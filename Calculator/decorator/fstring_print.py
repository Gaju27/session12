import math


def fstring_print(fn):
    def inner(value):
        output=fn(value)
        print(f'{fn.__name__} of {value}  is  {output}')
        return fn(value)
    return inner


# @print_f
# @fstring_print
# def sin_(value):
#     return math.sin(value)

# sin_(10)