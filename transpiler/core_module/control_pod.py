from transpiler.core_module.statement_pod import Statement
from ..sub_module.key_words import IF, ELSE, ELIF
from ..sub_module.sign import LEFT_BRACE, RIGHT_BRACE, ASSIGNMENT, SEMICOLON


def get_conditional(left_value, right_value, sign):
    return f"{left_value} {sign} {right_value}"


class IfControl(Statement):

    def __init__(self, left_value, right_value, sign, body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.body = body

    def get(self):
        return f"{IF} {get_conditional(self.left_value, self.right_value, self.sign)} {LEFT_BRACE} \n{self.body}" \
               f"\n{RIGHT_BRACE}"


class IfElseControl(Statement):
    def __init__(self, left_value, right_value, sign, if_body, else_body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.if_body = if_body
        self.else_body = else_body

    def get(self) -> str:
        return f"{IF} {get_conditional(self.left_value, self.right_value, self.sign)} {LEFT_BRACE}" \
               f"\n{self.if_body}\n" \
               f"{RIGHT_BRACE} {ELSE} {LEFT_BRACE}" \
               f"\n{self.else_body}\n" \
               f"{RIGHT_BRACE}"


class IfElifElseControl(Statement):
    def __init__(self):
        pass

    def get(self):
        pass
