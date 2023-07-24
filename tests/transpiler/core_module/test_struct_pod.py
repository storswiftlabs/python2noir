import unittest

from transpiler.core_module import Struct, StructGenerics
from transpiler.sub_module.key_words import SELF
from transpiler.sub_module.primitive_type import FIELD, array_type, N


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

    def test_impl_struct_fn(self):
        struct_name = "Dataset"
        name_and_type = {"bar": FIELD, "baz": array_type(FIELD, N)}
        my_struct = Struct(struct_name, name_and_type)
        print("struct:\n", my_struct.generate_noir_struct())
        some_fn1 = my_struct.generate_struct_fn("some_fn1", {"self": SELF}, FIELD,
                                                ["self.bar + self.baz[0] + self.baz[1]"])
        some_fn2 = my_struct.generate_struct_fn("some_fn2", {"self": SELF}, FIELD,
                                                ["self.bar + self.baz[0] + self.baz[1]"])
        impl_list = [some_fn1, some_fn2]
        print("struct impl:\n", my_struct.impl_struct_fn(impl_list))
        assert my_struct.impl_struct_fn(impl_list) == """impl Dataset { 
fn some_fn1(self : Self,) -> pub Field {
self.bar + self.baz[0] + self.baz[1]
}fn some_fn2(self : Self,) -> pub Field {
self.bar + self.baz[0] + self.baz[1]
}}
"""

    def test_impl_struct_fn_generics(self):
        struct_name = "Dataset"
        name_and_type = {"bar": FIELD, "baz": array_type(FIELD, 2)}
        my_struct = StructGenerics(struct_name, name_and_type, generics_type=True, generics_num=True)
        print("struct:\n", my_struct.generate_noir_struct())
        some_fn1 = my_struct.generate_struct_fn("some_fn1", {"self": SELF}, FIELD,
                                                ["self.bar + self.baz[0] + self.baz[1]"])
        some_fn2 = my_struct.generate_struct_fn("some_fn2", {"self": SELF}, FIELD,
                                                ["self.bar + self.baz[0] + self.baz[1]"])
        impl_list = [some_fn1, some_fn2]
        print("struct impl:\n", my_struct.impl_struct_fn(impl_list))
        assert my_struct.impl_struct_fn(impl_list) == """impl<T, N> Dataset<T, N> { 
fn some_fn1(self : Self,) -> pub Field {
self.bar + self.baz[0] + self.baz[1]
}fn some_fn2(self : Self,) -> pub Field {
self.bar + self.baz[0] + self.baz[1]
}}
"""
