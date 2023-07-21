import unittest
from transpiler.core_module.func_pod import Function


class test_func_pod(unittest.TestCase):
    def test_func_pod(self):
        inputs_variate_and_type = {'x': 'Field', 'y': 'Field'}
        body = ['x + y']
        result = Function("main", inputs_variate_and_type, 'Field', body).get()
        print(result)


if __name__ == '__main__':
    unittest.main()
