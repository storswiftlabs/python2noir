from abc import ABC, abstractmethod

from transpiler.sub_module.key_words import FN
from transpiler.sub_module.sign import LEFT_PARENTHESIS, RIGHT_PARENTHESIS, LEFT_BRACE, RIGHT_BRACE


class Func(ABC):
    """
    Code function:The function body contains a set of functions that define the task the function performs.
    """

    @abstractmethod
    def get(self):
        pass
        # Get a line code function


class Function(Func):
    # Function: {fn} {variate} {global variable} ( {inputs} ) -> output {

    def __init__(self, fn_name: str, inputs_variate_and_type: dict, result_type: str, body: list):
        self.inputs_variate_and_type = ''
        self.fn_name = fn_name
        for key, value in inputs_variate_and_type.items():
            temp = key + " : " + value + ","
            self.inputs_variate_and_type += temp
        self.result_type = result_type
        self.body = body

    def get(self):
        return f"{FN} {self.fn_name}{LEFT_PARENTHESIS}{self.inputs_variate_and_type}{RIGHT_PARENTHESIS} " \
               f"-> pub {self.result_type} {LEFT_BRACE}\n{''.join(self.body)}\n{RIGHT_BRACE}"
