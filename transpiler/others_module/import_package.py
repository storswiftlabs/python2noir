from transpiler.core_module.statement_pod import Statement
from transpiler.sub_module.key_words import MOD, USE, DEP_STD, DEP_STD_PRINTLN
from transpiler.sub_module.sign import SEMICOLON


class Mod(Statement):
    def __init__(self, file_name):
        self.mod = f"{MOD} {file_name}{SEMICOLON}\n"

    def get(self):
        return self.mod


class Use:
    custom_use = ""
    def __init__(self):
        self.standard_library = f"{USE} {DEP_STD}{SEMICOLON}\n"
        self.standard_library_println = f"{USE} {DEP_STD_PRINTLN}{SEMICOLON}\n"

    def define_custom_use(self, use):
        self.custom_use = f"{USE} {use}{SEMICOLON}\n"
