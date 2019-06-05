import math

ARITHMETIC_OPERATORS = ['+', '-', '*', '/', '//', '%', '^']
COMPARISION_OPERATORS = ['<', '<=', '==', '!=', '>=', '>']
BUILD_IN_FUNCTIONS = ['abs', 'round']
LEFT_PAREN, RIGHT_PAREN = '(', ')'
PARENTHESES = [LEFT_PAREN, RIGHT_PAREN]


def get_operators_str():
    """Get a list of string representation of all operations and functions"""
    math_functions = [attr for attr in dir(math) if callable(getattr(math, attr)) and not attr.startswith('__')]
    return ARITHMETIC_OPERATORS + COMPARISION_OPERATORS + BUILD_IN_FUNCTIONS + math_functions + PARENTHESES
