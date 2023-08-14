from typing import Union, List

from transpiler.core_module.struct_pod import Struct, StructGenerics
from transpiler.core_module.func_pod import Function, FunctionGenerics
from transpiler.core_module.statement_pod import Global
from transpiler.others_module import Annotation
from transpiler.others_module.import_package import Use, Mod


class NoirContext:
    def __init__(self):
        # User init Noir_context, use context structure noir code
        """
        function_list []Func (func_type, func_data)
        struct_list []Struct
        variates {inputs：[], struct: [], map: [], let: []}
        """
        self.function_list = []
        self.struct_list = []
        self.variates = dict()
        self.global_list = []
        self.use_list = []
        self.mod_list = []
        self.annotations = []

    def add_struct(self, struct_name, name_and_type: dict):
        # Define a structure
        noir_struct = Struct(struct_name, name_and_type)
        self.struct_list.append(noir_struct)

    def add_struct_generics(self, struct_name, name_and_type: dict, generics_type, generics_num):
        # Define a structure
        noir_struct = StructGenerics(struct_name, name_and_type, generics_type, generics_num)
        self.struct_list.append(noir_struct)

    def generate_struct_and_impl_function(self, funcs: list):
        pass

    def get_struct_by_name(self, struct_name):
        for struct_obj in self.struct_list:
            if struct_obj.struct_name == struct_name:
                return struct_obj

    def generate_struct(self):
        noir_lines = []
        # Fill struct definition
        for struct in self.struct_list:
            noir_lines.append(struct.generate_noir_struct())
        return noir_lines

    def add_function(self, variate, inputs: dict, return_type, body):
        func = Function(variate, inputs, return_type, body)
        self.function_list.append(func)

    def add_function_generics(self, variate, inputs: dict, return_type, body, generics_type, generics_num):
        func = FunctionGenerics(variate, inputs, return_type, body, generics_type, generics_num)
        self.function_list.append(func)

    def add_global(self, inputs: tuple):
        noir_global = Global(inputs)
        self.global_list.append(noir_global)

    def generate_global(self):
        noir_lines = []
        for global_variate in self.global_list:
            noir_lines.append(global_variate.get())
        return noir_lines

    # TODO: There are too few operating methods for `use`
    def add_use(self, use_statement):
        use = Use()
        use.define_custom_use(use_statement)
        self.use_list.append(use.custom_use)

    def generate_use(self):
        noir_list = []
        for use_variate in self.use_list:
            noir_list.append(use_variate)
        return noir_list

    def add_mod(self, fn_name):
        use = Mod(fn_name)
        self.mod_list.append(use)

    def generate_mod(self):
        noir_list = []
        for mod_variate in self.mod_list:
            noir_list.append(mod_variate.get())
        return noir_list

    def add_annotation(self, line, content):
        annotation = Annotation(line, content)
        self.annotations.append(annotation)

    def append_annotation(self, noir_lines: list):
        for annotation_obj in self.annotations:
            noir_lines.insert(annotation_obj.line, annotation_obj.get_content())
        return noir_lines

    def generate_noir_code_list(self):
        self.add_annotation(0, "Code generated from Python2Noir")
        noir_lines = []
        # Fill struct definition
        for use in self.use_list:
            noir_lines.append(use)
        for mod in self.mod_list:
            noir_lines.append(mod.get())
        for variate in self.global_list:
            noir_lines.append(variate.get()+'\n')
        for struct in self.struct_list:
            noir_lines.append(struct.generate_noir_struct())
        # Fill function
        for func in self.function_list:
            noir_lines.append(func.get())
        noir_lines = self.append_annotation(noir_lines)
        return noir_lines
