import unittest
from transpiler.core_module.control_pod import If_control, Elif_control, Else_control, If_else_control
from transpiler.sub_module.sign import LESS_THAN, GREATER_THAN, SEMICOLON


class test_control_pod(unittest.TestCase):

    def test_If_Control(self):
        left_value = 'a'
        right_value = 'b'
        sign = LESS_THAN
        body = "true"
        result = If_control(left_value, right_value, sign, body).get()
        print(result)

    def test_If_Else_Control(self):
        left_value = 'a'
        right_value = 'b'
        sign = LESS_THAN
        if_body = "true"
        else_body = "false"
        result = If_else_control(left_value, right_value, sign, if_body, else_body).get()
        print(result)

    def test_If_ElIf_Else_Control(self):
        output = ''
        output += If_control('inputs.p1', '100', str(GREATER_THAN), f"println(1)").get()
        output += Elif_control('inputs.p1', '80', str(GREATER_THAN), f"println(2)").get()
        output += Else_control(f"println(3)").get()
        print(output)
