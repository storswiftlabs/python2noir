from abc import ABC, abstractmethod

from transpiler.sub_module.key_words import FN, N, PUB, T
from transpiler.sub_module.sign import LEFT_PARENTHESIS, RIGHT_PARENTHESIS, LEFT_BRACE, RIGHT_BRACE, RESULT, COMMA, \
    LESS_THAN, GREATER_THAN
from transpiler.utils import log


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
        self.body = ''.join(body)

    def get(self):
        if self.result_type == '':
            return f"{FN} {self.fn_name}{LEFT_PARENTHESIS}{self.inputs_variate_and_type}{RIGHT_PARENTHESIS} " \
                f"{LEFT_BRACE}\n{self.body}\n{RIGHT_BRACE}\n"
        else:
            return f"{FN} {self.fn_name}{LEFT_PARENTHESIS}{self.inputs_variate_and_type}{RIGHT_PARENTHESIS} " \
               f"{RESULT} {PUB} {self.result_type} {LEFT_BRACE}\n{self.body}\n{RIGHT_BRACE}\n"


class FunctionGenerics(Function):
    # Function: {fn} {variate} {global variable} ( {inputs} ) -> output {

    def __init__(self, fn_name: str, inputs_variate_and_type: dict, result_type: str, body: list,
                 generics_type: bool = False, generics_num: bool = False):
        super().__init__(fn_name, inputs_variate_and_type, result_type, body)

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

    def get(self):
        if not self.first_generics and not self.second_generics:
            log.warning("Inputs generics args is None which both 'generics_type' and 'generics_num'")
            return super().get()

        return f"{FN} {self.fn_name}{self.generics_str}{LEFT_PARENTHESIS}{self.inputs_variate_and_type}" \
               f"{RIGHT_PARENTHESIS} {RESULT} {PUB} {self.result_type} {LEFT_BRACE}\n{''.join(self.body)}\n{RIGHT_BRACE}\n"


class Closure(Func):
    # {FN} {variate}{LEFT_PARENTHESIS}{inputs_dict}{RIGHT_PARENTHESIS} {RESULT} {res_type}{LEFT_BRACE} {exp} {RIGHT_BRACE}
    # fn bar(x: Field) -> Field { x + 1 }
    def __init__(self, variate, inputs_dict: dict, exp: list, res_type):
        self.closure_statement = f"{FN} {variate}{LEFT_PARENTHESIS}{inputs_dict}{RIGHT_PARENTHESIS} " \
                                 f"{RESULT} {res_type}{LEFT_BRACE} {exp} {RIGHT_BRACE}"

    def get(self):
        return self.closure_statement
