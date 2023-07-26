from transpiler.core_module.statement_pod import Statement
from transpiler.sub_module.key_words import MOD, USE, DEP_STD, DEP_STD_PRINTLN
from transpiler.sub_module.sign import SEMICOLON


class Mod(Statement):
    def __init__(self, file_name):
        self.mod = f"{MOD} {file_name}{SEMICOLON}\n"

    def get(self):
        return self.mod


class Use:
    def standard_library(self):
        return f"{USE} {DEP_STD}{SEMICOLON}\n"

    def standard_library_println(self):
        return f"{USE} {DEP_STD_PRINTLN}{SEMICOLON}\n"

    def custom_use(self, use):
        return f"{USE} {use}{SEMICOLON}\n"
