import unittest
from transpiler.context.noir_context import NoirContext
from transpiler.core_module.statement_pod import Let
from transpiler.sub_module.key_words import LET
from transpiler.sub_module.primitive_type import Uint32
from transpiler.utils.utils import table_format_control


class test_context(unittest.TestCase):
    def test_add_struct(self):
        struct_name = "Axis"
        name_and_type = {'node_name': 'u8', 'right': 'bool', 'left': 'bool'}
        context = NoirContext()
        context.add_struct(struct_name, name_and_type)
        struct_str = ""
        for line in context.generate_struct():
            struct_str += line
        print(struct_str)
        self.assertTrue(struct_str, """struct Axis { 
    node_name: u8;
    right: bool;
    left: bool;
    }""")

    def test_generate_Noir(self):
        global_value = ('N', "Field", 5)
        struct_name = "Axis"
        name_and_type = {'node_name': 'u8', 'right': 'bool', 'left': 'bool'}
        context = NoirContext()
        context.add_struct(struct_name, name_and_type)
        variate = 'main'
        u32 = Uint32
        input1 = 'x'
        context.add_global(global_value)
        context.add_function(variate, name_and_type, u32, generate_body())

        data_arr = context.generate_noir_code_list()
        data_arr = table_format_control(data_arr)
        transition_str = ""
        for line in data_arr:
            transition_str += line
        print(transition_str)


def generate_body():
    body = []
    let = LET
    variate = 'a'
    variate_type = Uint32
    variate_body = '9'
    l = Let(variate, variate_type, variate_body, False)
    body.append(l.get())
    # add return
    body.append(variate)
    print(body)
    return body


if __name__ == '__main__':
    unittest.main()
