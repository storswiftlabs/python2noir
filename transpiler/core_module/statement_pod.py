from abc import ABC, abstractmethod

from ..sub_module.key_words import ASSERT, LET, IF, ELSE, MUT, FN, GLOBAL
from ..sub_module.sign import LEFT_PARENTHESIS, RIGHT_PARENTHESIS, SEMICOLON, LEFT_BRACE, RIGHT_BRACE, POINT, COMMA, \
    RESULT, ASSIGNMENT, COLON
from transpiler.core_module.struct_pod import Struct


class Statement(ABC):
    """
    Code statement:The function body contains a set of statements that define the task the function performs.
    """

    @abstractmethod
    def get(self):
        pass
        # Get a line code statement


class Let(Statement):
    # let statement: {let} {variate}: {variate_type} = {variate_body};

    def __init__(self, variate, variate_type, variate_body, is_mut: bool):
        # Get a line code statement
        self.variate = variate
        if is_mut:
            self.let_statement = f"{LET} mut {variate}: {variate_type} {ASSIGNMENT} {variate_body}{SEMICOLON}"
        else:
            self.let_statement = f"{LET} {variate}: {variate_type} {ASSIGNMENT} {variate_body}{SEMICOLON}"

    def get(self):
        # Get a line code statement
        return self.let_statement


class Assert(Statement):
    # {assert}{LEFT_PARENTHESIS}{conditional}{RIGHT_PARENTHESIS}{SEMICOLON}
    # assert (s.sum() == 42);
    # assert(array_eq(array, array, MyStruct::eq));
    # assert (array_eq([1, 2, 3], [1, 2, 3], | a, b | a == b));

    def __init__(self, conditional):
        self.assert_statement = f"{ASSERT}{LEFT_PARENTHESIS}{conditional}{RIGHT_PARENTHESIS}{SEMICOLON}"

    def get(self):
        # Get a line code statement
        return self.assert_statement


class If_single_raw(Statement):
    # Ternary expression
    # {LET} {variate} = {IF} {exp} {LEFT_BRACE}{if_exp}{RIGHT_BRACE} {ELSE} {LEFT_BRACE}{else_exp}{RIGHT_BRACE}{SEMICOLON}
    # let (a, b) = if true { (0, 1) } else { (2, 3) };
    def __init__(self, variate, bool_exp, if_exp, else_exp):
        self.variate = variate
        self.if_single_raw_statement = f"{LET} {variate} {ASSIGNMENT} {IF} {bool_exp} {LEFT_BRACE}{if_exp}" \
                                       f"{RIGHT_BRACE} {ELSE} {LEFT_BRACE}{else_exp}{RIGHT_BRACE}{SEMICOLON}"

    def get(self):
        return self.if_single_raw_statement


class Tuple(Statement):
    # {LET} {variate} = {exp}{SEMICOLON}
    # let (a, b) = (0, 1);
    def __init__(self, variate, exp, is_mut: bool):
        self.variate = variate
        if is_mut:
            self.tuple_statement = f"{LET} {MUT} {variate} {ASSIGNMENT} {exp}{SEMICOLON}"
        else:
            self.tuple_statement = f"{LET} {variate} {ASSIGNMENT} {exp}{SEMICOLON}"

    def get(self):
        return self.tuple_statement


class Array(Statement):
    # Ternary expression
    # {LET} {variate} = {exp}{SEMICOLON}
    # let arr = [0, 1];
    # let arr: [Field; 2] = [0, 1];
    # XXX: 1 exp: str; 2 multi_type_check; 3 is_define_type: add a arg
    def __init__(self, variate, exp, is_mut):
        self.variate = variate
        variate = str(variate)
        if is_mut:
            self.array_statement = f"{LET} {MUT} {variate} {ASSIGNMENT} {exp}{SEMICOLON}"
        else:
            self.array_statement = f"{LET} {variate} {ASSIGNMENT} {exp}{SEMICOLON}"

    def get(self):
        return self.array_statement

    def array_len(self):
        array_len = 'len()'
        return f"{self.variate}{POINT}{array_len}"

    def array_sort(self):
        array_sort = 'sort()'
        return f"{self.variate}{POINT}{array_sort}"

    def array_sort_via(self, sort_lambda):
        array_sort_via = f'sort_via({sort_lambda})'
        return f"{self.variate}{POINT}{array_sort_via}"

    def array_map(self, map_lambda):
        array_map = f'map({map_lambda})'
        return f"{self.variate}{POINT}{array_map}"

    def array_fold(self, start_index: int, fold_lambda):
        array_fold = f'fold({start_index}{COMMA} {fold_lambda})'
        return f"{self.variate}{POINT}{array_fold}"

    def array_reduce(self, reduce_lambda):
        array_reduce = f'reduce({reduce_lambda})'
        return f"{self.variate}{POINT}{array_reduce}"

    def array_all(self, all_lambda):
        array_all = f'all({all_lambda})'
        return f"{self.variate}{POINT}{array_all}"

    def array_any(self, any_lambda):
        array_any = f'any({any_lambda})'
        return f"{self.variate}{POINT}{array_any}"


class Lambda(Statement):
    # Ternary expression
    # {LET} {variate} = {exp}{SEMICOLON}
    # let some_closure = |x| 42 - x;
    # XXX: lambda exp check
    def __init__(self, variate, exp, is_mut: bool):
        self.variate = variate
        if is_mut:
            self.lambda_statement = f"{LET} {MUT} {variate} {ASSIGNMENT} {exp}{SEMICOLON}"
        else:
            self.lambda_statement = f"{LET} {variate} {ASSIGNMENT} {exp}{SEMICOLON}"

    def get(self):
        return self.lambda_statement


class Let_struct(Statement):
    # let_struct statement: {let} {struct_name}
    """
    define:
        1. let octopus = Animal {hands: 0,legs: 8,eyes: 2};
    receive
        1. let Animal { hands, legs, eyes } = get_octopus();
        2. let octopus : Animal = get_octopus();
    """

    def __init__(self, struct: Struct, variate, body):
        self.struct = struct
        self.variate = variate
        self.body = body

    def get(self):
        """
        let octopus = Animal {hands: 0,legs: 8,eyes: 2};
        """
        struct = f"{LET} {self.variate} {ASSIGNMENT} {self.struct.struct_name} {LEFT_BRACE}"
        for key, value in self.struct.name_and_type.items():
            struct += f"{key}{COLON} {value}{COMMA}"
        struct += f"{RIGHT_BRACE}{SEMICOLON}"
        return struct

    def get_for_variate(self):
        """
        let Animal { hands, legs, eyes } = get_octopus();
        """
        variate = []
        for key, value in self.struct.name_and_type.items():
            variate.append(key)
        return f"{LET} {self.struct.struct_name} {LEFT_BRACE}{','.join(variate)}{RIGHT_BRACE} {ASSIGNMENT} " \
               f"{self.body}{SEMICOLON}"


class Global(Statement):

    # 传入元组，或者数组
    def __init__(self, inputs: tuple):
        self.global_variate = f"{GLOBAL} {inputs[0]} : {inputs[1]} {ASSIGNMENT} {inputs[2]}{SEMICOLON}"

    def get(self):
        return self.global_variate
