import unittest
from transpiler.core_module.control_pod import IfControl, IfElseControl
from transpiler.sub_module.sign import LESS_THAN, GREATER_THAN
from transpiler.utils.utils import table_format_control


class test_control_pod(unittest.TestCase):

    def test_If_Control(self):
        left_value = 'a'
        right_value = 'b'
        sign = LESS_THAN
        body = "true"
        result = IfControl(left_value, right_value, sign, body).get()
        print(result)
        self.assertTrue(result, """if a < b { 
true
}""")

    def test_If_Else_Control(self):
        left_value = 'a'
        right_value = 'b'
        sign = LESS_THAN
        if_body = "true"
        else_body = "false"
        result = IfElseControl(left_value, right_value, sign, if_body, else_body).get()
        print(result)
        self.assertTrue(result, """if a < b { 
true
} else { 
false
} """)

    def test_If_ElIf_Else_Control(self):
        pass
