import unittest

from transpiler.core_module.statement_pod import Assert, If_single_raw, Tuple, Array, Lambda


class test_statement_pod(unittest.TestCase):
    def test_assert(self):
        conditional = "s.sum() == 42"
        my_assert = Assert(conditional)
        print(my_assert.get())
        assert "assert(s.sum() == 42);" == my_assert.get()

    def test_if_single_raw(self):
        conditional = "s.sum() == 42"
        variate = "(a, b)"
        bool_exp = "true"
        if_exp = "(0, 1)"
        else_exp = "(2, 3)"
        my_if_single_raw = If_single_raw(variate, bool_exp, if_exp, else_exp)
        print(my_if_single_raw.get())
        assert "let (a, b) = if true {(0, 1)} else {(2, 3)};" == my_if_single_raw.get()

    def test_tuple(self):
        variate = "(a, b)"
        exp = (0, 1)
        is_mut = True
        my_tuple_mut = Tuple(variate, exp, is_mut)
        print(my_tuple_mut.get())
        assert "let mut (a, b) = (0, 1);" == my_tuple_mut.get()
        my_tuple = Tuple(variate, exp, not is_mut)
        print(my_tuple.get())
        assert "let (a, b) = (0, 1);" == my_tuple.get()

    def test_array(self):
        variate = "arr"
        exp = [0, 1]
        is_mut = True
        my_array_mut = Array(variate, exp, is_mut)
        print(my_array_mut.get())
        assert "let mut arr = [0, 1];" == my_array_mut.get()
        my_array = Array(variate, exp, not is_mut)
        print(my_array.get())
        assert "let arr = [0, 1];" == my_array.get()

    def test_array_methods(self):
        variate = "arr"
        exp = [0, 1]
        is_mut = False
        my_array = Array(variate, exp, is_mut)
        my_len = my_array.array_len()
        assert "arr.len()" == my_len
        my_sort = my_array.array_sort()
        assert "arr.sort()" == my_sort
        my_sort_via = my_array.array_sort_via("|a, b| a > b")
        assert "arr.sort_via(|a, b| a > b)" == my_sort_via
        my_map = my_array.array_map("|a| a * 2")
        assert "arr.map(|a| a * 2)" == my_map
        my_fold = my_array.array_fold(0, "|a, b| a - b")
        assert "arr.fold(0, |a, b| a - b)" == my_fold
        my_reduce = my_array.array_reduce("|a, b| a - b")
        assert "arr.reduce(|a, b| a - b)" == my_reduce
        my_all = my_array.array_all("|a| a == 2")
        assert "arr.all(|a| a == 2)" == my_all
        my_any = my_array.array_any("|a| a == 2")
        assert "arr.any(|a| a == 2)" == my_any

    def test_lambda(self):
        variate = "some_closure"
        exp = "|x| 42 - x"
        is_mut = True
        my_lambda_mut = Lambda(variate, exp, is_mut)
        print(my_lambda_mut.get())
        assert "let mut some_closure = |x| 42 - x;" == my_lambda_mut.get()
        my_lambda = Array(variate, exp, not is_mut)
        print(my_lambda.get())
        assert "let some_closure = |x| 42 - x;" == my_lambda.get()
