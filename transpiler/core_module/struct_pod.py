from ..sub_module.key_words import STRUCT, IMPL, T, N
from ..sub_module.sign import LEFT_BRACE, RIGHT_BRACE, COLON, COMMA, LESS_THAN, GREATER_THAN
from ..utils import log


class Struct:
    def __init__(self, struct_name, name_and_type: dict):
        #  generate struct for context
        self.struct_name = struct_name
        self.name_and_type = name_and_type

    def generate_noir_struct(self) -> str:
        # return a string, Noir defined code style, for example ""
        struct_multi_lines = f"{STRUCT} {str(self.struct_name)} {LEFT_BRACE} \n"
        for k, v in self.name_and_type.items():
            struct_multi_lines += f"{k}{COLON} {v}{COMMA}\n"
        struct_multi_lines += f"{RIGHT_BRACE}\n"
        return struct_multi_lines

    def impl_struct_fn(self, functions: list) -> str:
        struct_fn_multi_lines = f"{IMPL} {self.struct_name} {LEFT_BRACE} \n"
        for func in functions:
            struct_fn_multi_lines += func
        struct_fn_multi_lines += f"{RIGHT_BRACE}\n"
        return struct_fn_multi_lines

    def generate_struct_fn(self) -> str:
        # XXX: wait import function_pod
        pass


class StructGenerics(Struct):
    def __init__(self, struct_name, name_and_type: dict, generics_type: bool = False, generics_num: bool = False):
        super().__init__(struct_name, name_and_type)

        self.first_generics = ""
        self.second_generics = ""

        if generics_type:
            self.first_generics = T
        if generics_num:
            if self.first_generics:
                self.second_generics = f"{COMMA} {N}"
            else:
                self.first_generics = N
        self.generics_str = f"{LESS_THAN}{self.first_generics}{self.second_generics}{GREATER_THAN}"

    def generate_noir_struct(self) -> str:
        # return a string, Noir defined code style, for example ""
        if not self.first_generics and not self.second_generics:
            log.warning("Inputs generics args is None which both 'generics_type' and 'generics_num'")
            return super().generate_noir_struct()

        struct_multi_lines = f"{STRUCT} {str(self.struct_name)}{self.generics_str} {LEFT_BRACE} \n"
        for k, v in self.name_and_type.items():
            struct_multi_lines += f"{k}{COLON} {v}{COMMA}\n"
        struct_multi_lines += f"{RIGHT_BRACE}\n"

        return struct_multi_lines

    def impl_struct_fn(self, functions: list) -> str:
        if not self.first_generics and not self.second_generics:
            log.warning("Inputs generics args is None which both 'generics_type' and 'generics_num'")
            return super().impl_struct_fn(functions)

        struct_fn_multi_lines = f"{IMPL}{self.generics_str} {self.struct_name}{self.generics_str} {LEFT_BRACE} \n"
        for func in functions:
            struct_fn_multi_lines += func
        struct_fn_multi_lines += f"{RIGHT_BRACE}\n"
        return struct_fn_multi_lines

    def generate_struct_fn(self) -> str:
        # XXX: wait import function_pod
        pass
        return super().generate_struct_fn()
