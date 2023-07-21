from transpiler.sub_module.key_words import STRUCT, IMPL
from transpiler.sub_module.sign import LEFT_BRACE, RIGHT_BRACE, COLON, COMMA


class Struct:
    def __init__(self, struct_name, name_and_type: dict):
        #  generate struct for context
        self.struct_name = struct_name
        self.name_and_type = name_and_type

    def generate_leo_struct(self) -> str:
        # return a string, Leo defined code style, for example ""
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
