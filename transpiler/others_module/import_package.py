from transpiler.core_module.statement_pod import Statement
from transpiler.sub_module.key_words import MOD, USE, DEP_STD
from transpiler.sub_module.sign import SEMICOLON


class Mod(Statement):
    def __init__(self, file_name):
        self.mod = f"{MOD} {file_name}{SEMICOLON}"

    def get(self):
        return self.mod


class Use(Statement):
    def __init__(self, fn_name):
        if fn_name == '':
            self.use = f"{USE} {DEP_STD}{SEMICOLON}\n"
        else:
            self.use = f"{USE} {DEP_STD}::{fn_name}{SEMICOLON}\n"

    def get(self):
        return self.use
