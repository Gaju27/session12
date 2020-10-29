import inspect
import math
import os
import re
import numpy as np

import Calculator

from Calculator import derivatives

README_CONTENT_CHECK_FOR = [
    'cos',
    'sin',
    'tan',
    'tanh',
    'sigmoid',
    'softmax',
    'exponential',
    'log',
    'derivatives'

]

path = 'image_store/'


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Calculator)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Calculator, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_cos():
    assert Calculator.cos_(45) == math.cos(45), "Check your Calculator cos Function"

def test_cos_derivative():
    assert derivatives.cos_d(45) == -math.sin(45), "Check your Calculator cos derivatives"

# def test_sin():
#     assert Calculator.sin_(45) == math.sin(45), "Check your Calculator sin Function"

def test_sin_derivative():
    assert derivatives.sin_d(45) == math.cos(45), "Check your Calculator sin derivatives"

def test_tan():
    assert Calculator.tan_(45) == math.tan(45), "Check your Calculator tan Function"

def test_tan_derivative():
    assert derivatives.tand_(45) == (1 / (math.cos(45) ** 2)), "Check your Calculator tan derivatives"

def test_tanh():
    assert Calculator.tan_h(45) == math.tanh(45), "Check your Calculator tanh Function"

def test_tanh_derivative():
    assert derivatives.tan_hd(45) == 1 - (math.tanh(45) ** 2), "Check your Calculator tanh derivatives"

def test_log():
    assert Calculator.log_(45) == math.log(45), "Check your Calculator log Function"

def test_log_derivative():
    assert derivatives.log_d(45) == 1 / 45, "Check your Calculator log derivatives"

def test_exp():
    assert Calculator.exponential(45) == math.exp(45), "Check your Calculator exp Function"

def test_exp_derivative():
    assert derivatives.exponential_d(45) == math.exp(45), "Check your Calculator log derivatives"

def test_relu():
    assert Calculator.relu_(1) == 1, "Check your Calculator relu Function"

def test_relu_derivative():
    assert derivatives.relu_d(-30) == 0, "Check your Calculator log derivatives"

def test_sigmoid():
    assert Calculator.sigmoid_(1) == 1 / (1 + math.exp(-1)) , "Check your Calculator relu Function"
