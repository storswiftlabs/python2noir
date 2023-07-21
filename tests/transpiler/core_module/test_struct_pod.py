import unittest

from transpiler.core_module.struct_pod import Struct, StructGenerics


class test_struct_pod(unittest.TestCase):
    def test_generate_noir_struct(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        my_struct = Struct(struct_name, name_and_type)
        print("struct:", my_struct.generate_noir_struct())
        assert my_struct.generate_noir_struct() == """struct Dataset { 
node: u32,
son_node_nums: u8,
level: u8,
weight: u16,
}
"""

    def test_generate_noir_struct_generics_all_none(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        my_struct = StructGenerics(struct_name, name_and_type)
        print("struct:", my_struct.generate_noir_struct())
        assert my_struct.generate_noir_struct() == """struct Dataset { 
node: u32,
son_node_nums: u8,
level: u8,
weight: u16,
}
"""

    def test_generate_noir_struct_generics_type_none(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        generics_num = True
        my_struct = StructGenerics(struct_name, name_and_type, generics_type=False, generics_num=generics_num)
        print("struct:", my_struct.generate_noir_struct())
        assert my_struct.generate_noir_struct() == """struct Dataset<N> { 
node: u32,
son_node_nums: u8,
level: u8,
weight: u16,
}
"""

    def test_generate_noir_struct_generics_number_none(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        generics_type = True
        my_struct = StructGenerics(struct_name, name_and_type, generics_type=generics_type)
        print("struct:", my_struct.generate_noir_struct())
        assert my_struct.generate_noir_struct() == """struct Dataset<T> { 
node: u32,
son_node_nums: u8,
level: u8,
weight: u16,
}
"""

    def test_generate_noir_struct_generics_all(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        generics_type = True
        generics_num = True
        my_struct = StructGenerics(struct_name, name_and_type, generics_type=generics_type, generics_num=generics_num)
        print("struct:", my_struct.generate_noir_struct())
        assert my_struct.generate_noir_struct() == """struct Dataset<T, N> { 
node: u32,
son_node_nums: u8,
level: u8,
weight: u16,
}
"""
