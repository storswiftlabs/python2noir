import unittest
from transpiler.core_module.func_pod import Function, FunctionGenerics
from transpiler.sub_module.primitive_type import array_type, T, N, FIELD


class test_func_pod(unittest.TestCase):
    def test_func_pod(self):
        inputs_variate_and_type = {'x': 'Field', 'y': 'Field'}
        body = ['x + y']
        result = Function("main", inputs_variate_and_type, 'Field', body).get()
        print(result)
        self.assertTrue(result, """fn main(x : Field,y : Field,) -> pub Field {
x + y
}""")

    def test_FunctionGenerics(self):
        inputs_variate_and_type = {'x': array_type(T, N), 'y': T}
        body = ['x[0] + y']
        my_function_generics = FunctionGenerics("bar", inputs_variate_and_type, 'Field', body, generics_type=True,
                                                generics_num=True)
        print("Function Generics:", my_function_generics.get())
        assert my_function_generics.get() == """fn bar<T, N>(x : [T; N],y : T,) -> pub Field {
x[0] + y
}"""

    def test_FunctionGenerics_impl_struct(self):
        inputs_variate_and_type = {'x': array_type(T, N), 'y': T}
        body = ['x[0] + y']
        my_function_generics = Function("bar", inputs_variate_and_type, 'Field', body)
        print("Function Generics:", my_function_generics.get())
        assert my_function_generics.get() == """fn bar(x : [T; N],y : T,) -> pub Field {
x[0] + y
}"""


if __name__ == '__main__':
    unittest.main()
