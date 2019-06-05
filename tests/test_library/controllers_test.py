import unittest
from final_task.library.controllers import convert_controller


class ConvertControllerTest(unittest.TestCase):
    def test_prepare_function(self):
        expression = '(2.34+4)*1.4^0.456-sin(round(4.7)*pi)==0'
        test_expression = convert_controller._prepare_expression_for_conversion(expression)
        correct_expression = '( 2.34 + 4 ) * 1.4 ^ 0.456 - sin ( round ( 4.7 ) * pi ) == 0'.split()
        self.assertEqual(correct_expression, test_expression)
