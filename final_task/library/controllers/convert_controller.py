import re
import library.entities.tokens as tokens

WHITESPACE = ' '
EMPTY_CHARACTER = ''


def _prepare_expression_for_conversion(expression):
    """Remove whitespace and convert an expression to a list of operations, functions, and numbers."""
    operators = r'(' + '|'.join(list(map(re.escape, tokens.get_operators_str()))) + r')'
    expression_without_space_s = expression.replace(WHITESPACE, EMPTY_CHARACTER).lower()
    prepared_expression_l = re.sub(operators, r' \1 ', expression_without_space_s)
    return prepared_expression_l.split()

