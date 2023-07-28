from typing import Union, List

from transpiler.core_module.struct_pod import Struct
from transpiler.core_module.func_pod import Function
from transpiler.core_module.statement_pod import Global
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

    def add_struct(self, struct_name, name_and_type: dict):
        # Define a structure
        noir_struct = Struct(struct_name, name_and_type)
        self.struct_list.append(noir_struct)

    def get_struct_by_name(self, struct_name):
        for struct_obj in self.struct_list:
            if struct_obj.struct_name == struct_name:
                return struct_obj

    def add_function(self, variate, inputs: dict, return_type, body):
        func = Function(variate, inputs, return_type, body)
        self.function_list.append(func)

    def generate_struct(self):
        noir_lines = []
        # Fill struct definition
        for struct in self.struct_list:
            noir_lines.append(struct.generate_noir_struct())
        return noir_lines

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

    def add_mod(self, fn_name):
        use = Mod(fn_name)
        self.mod_list.append(use)

    def generate_mod(self):
        noir_list = []
        for mod_variate in self.mod_list:
            noir_list.append(mod_variate.get())

    def generate_noir_code_list(self, noir_name="main", fixed_number=1):
        noir_lines = [f"// Code generated from Python2Noir\n", f"// Fixed number is {fixed_number}\n\n"]
        # Fill struct definition
        for use in self.use_list:
            noir_lines.append(use)
        for mod in self.mod_list:
            noir_lines.append(mod.get())
        for variate in self.global_list:
            noir_lines.append(variate.get())
        for struct in self.struct_list:
            noir_lines.append(struct.generate_noir_struct())
        # Fill function
        for func in self.function_list:
            noir_lines.append(func.get())
        return noir_lines

