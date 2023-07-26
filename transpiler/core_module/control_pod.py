from transpiler.core_module.statement_pod import Statement
from ..sub_module.key_words import IF, ELSE, ELIF
from ..sub_module.sign import LEFT_BRACE, RIGHT_BRACE, ASSIGNMENT, SEMICOLON


def get_conditional(left_value, right_value, sign):
    return f"{left_value} {sign} {right_value}"


class If_control(Statement):

    def __init__(self, left_value, right_value, sign, body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.body = body

    def get(self):
        return f"{IF} {get_conditional(self.left_value, self.right_value, self.sign)} {LEFT_BRACE} \n{self.body}" \
               f"{SEMICOLON}\n{RIGHT_BRACE}\n"


class Elif_control(Statement):

    def __init__(self, left_value, right_value, sign, body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.body = body

    def get(self):
        if self.body == '':
            return ''
        return f"{ELIF} {get_conditional(self.left_value, self.right_value, self.sign)}  " \
               f"{LEFT_BRACE} \n{self.body}{SEMICOLON}\n{RIGHT_BRACE}\n"


class Else_control(Statement):
    def __init__(self, body):
        self.body = body

    def get(self):
        if self.body == '':
            return ''

        return f"{ELSE} {LEFT_BRACE} " \
               f"\n{self.body}{SEMICOLON}\n{RIGHT_BRACE}\n"


class If_else_control(Statement):
    def __init__(self, left_value, right_value, sign, if_body, else_body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.if_body = if_body
        self.else_body = else_body

    def get(self):
        # fixme: Line break issue waiting for processing
        return If_control(self.left_value, self.right_value, self.sign, self.if_body).get() + \
            " " + Else_control(self.else_body).get()
