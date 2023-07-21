from abc import ABC, abstractmethod
from logging import getLogger

from ..sub_module.key_words import ASSERT, LET, IF, ELSE, MUT, FN
from ..sub_module.sign import LEFT_PARENTHESIS, RIGHT_PARENTHESIS, SEMICOLON, LEFT_BRACE, RIGHT_BRACE, POINT, COMMA, \
    RESULT

log = getLogger(__name__)


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

    def __init__(self, variate, variate_type, variate_body):
        # Get a line code statement
        self.variate = variate
        self.let_statement = f"{LET} {variate}: {variate_type} = {variate_body};"

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
        self.if_single_raw_statement = f"{LET} {variate} = {IF} {bool_exp} {LEFT_BRACE}{if_exp}{RIGHT_BRACE} {ELSE} {LEFT_BRACE}{else_exp}{RIGHT_BRACE}{SEMICOLON}"

    def get(self):
        return self.if_single_raw_statement


class Tuple(Statement):
    # {LET} {variate} = {exp}{SEMICOLON}
    # let (a, b) = (0, 1);
    def __init__(self, variate, exp, is_mut: bool):
        self.variate = variate
        if is_mut:
            self.tuple_statement = f"{LET} {MUT} {variate} = {exp}{SEMICOLON}"
        else:
            self.tuple_statement = f"{LET} {variate} = {exp}{SEMICOLON}"

    def get(self):
        return self.tuple_statement


class Array(Statement):
    # Ternary expression
    # {LET} {variate} = {exp}{SEMICOLON}
    # let arr = [0, 1];
    # XXX: 1 exp: str; 2 multi_type_check
    def __init__(self, variate, exp, is_mut):
        self.variate = variate
        variate = str(variate)
        if is_mut:
            self.array_statement = f"{LET} {MUT} {variate} = {exp}{SEMICOLON}"
        else:
            self.array_statement = f"{LET} {variate} = {exp}{SEMICOLON}"

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
        if is_mut:
            self.lambda_statement = f"{LET} {MUT} {variate} = {exp}{SEMICOLON}"
        else:
            self.lambda_statement = f"{LET} {variate} = {exp}{SEMICOLON}"

    def get(self):
        return self.lambda_statement


class Closure(Statement):
    # {FN} {variate}{LEFT_PARENTHESIS}{inputs_dict}{RIGHT_PARENTHESIS} {RESULT} {res_type}{LEFT_BRACE} {exp} {RIGHT_BRACE}
    # fn bar(x: Field) -> Field { x + 1 }
    def __init__(self, variate, inputs_dict: dict, exp: list, res_type):
        self.closure_statement = f"{FN} {variate}{LEFT_PARENTHESIS}{inputs_dict}{RIGHT_PARENTHESIS} " \
                                 f"{RESULT} {res_type}{LEFT_BRACE} {exp} {RIGHT_BRACE}"

    def get(self):
        return self.closure_statement
