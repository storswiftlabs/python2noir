from transpiler.core_module.statement_pod import Statement
from ..sub_module.key_words import FOR, IN
from ..sub_module.sign import LEFT_BRACE, RIGHT_BRACE, SEMICOLON


class ForLoop(Statement):

    def __init__(self, variate, start_variate, end_variate, body):
        if start_variate == '':
            self.for_loop = f"{FOR} {variate} {IN} {end_variate}" \
                            f" {LEFT_BRACE} \n{body}\n{RIGHT_BRACE}\n"
        else:
            self.for_loop = f"{FOR} {variate} {IN} {start_variate}..{end_variate}" \
                            f" {LEFT_BRACE} \n{body}\n{RIGHT_BRACE}\n"

    def get(self):
        return self.for_loop
