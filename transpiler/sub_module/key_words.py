USE = 'use'
MOD = 'mod'
LET = 'let'
MUT = 'mut'
ASSERT = 'assert'
THEN = 'then'
RETURN = 'return'
IN = 'in'
PUB = 'pub'
PRINTLN = 'println'
DEP_STD_PRINTLN = f'dep::std::{PRINTLN}'

# comptime variables
COMPTIME = "comptime"

GLOBAL = 'global'
SELF = 'self'

"""
"\t" number +1 key words
"""
FOR = 'for'
IF = 'if'
ELSE = 'else'
ELIF = f'{ELSE} {IF}'
FN = 'fn'
STRUCT = 'struct'
IMPL = 'impl'
INLINE = 'inline'

# GET_TABLE_P_ONE = [FOR, IF, ELSE, ELIF, FN, STRUCT]
