import unittest
from transpiler.sub_module.primitive_type import custom_type, set_str


class test_primitive_type(unittest.TestCase):
    def test_custom_type(self):
        value = custom_type('u126')
        print(value)

    def test_set_str(self):
        value = set_str(18)
        print(value)
