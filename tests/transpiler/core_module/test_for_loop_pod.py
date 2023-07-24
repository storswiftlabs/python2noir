import unittest
from transpiler.core_module.for_loop_pod import ForLoop
from transpiler.core_module.statement_pod import Array


class test_for_loop_pod(unittest.TestCase):

    def test_for_loop_base(self):
        variate = 'i'
        start_variate = '0'
        end_variate = '10'
        body = 'sum += i'
        result = ForLoop(variate, start_variate, end_variate, body).get()
        print(result)

        arr_variate = 'arr'
        exp = [1, 2, 3, 4, 5]
        arr = Array(arr_variate, exp, False)

        result = ForLoop(variate, start_variate, arr.array_len(), 'println(i)').get()
        print(result)

        result = ForLoop(variate, '', arr.variate, 'println(i)').get()
        print(result)
