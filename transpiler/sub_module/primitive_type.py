from .sign import LESS_THAN, GREATER_THAN

# Primitive type
INT8 = 'i8'
INT16 = 'i16'
INT32 = 'i32'
INT64 = 'i64'
INT126 = 'i126'
UINT8 = 'u8'
UINT16 = 'u16'
UINT32 = 'u32'
UINT64 = 'u64'
UINT126 = 'u126'
BoolType = 'bool'
FIELD = 'Field'

PRIMITIVE_TYPE = [INT8, INT16, INT32, INT64, INT126, UINT8, UINT16, UINT32, UINT64, UINT126, BoolType, FIELD]
# Generics
T = 'T'
N = 'N'
GENERICS = [T, N]

# Boolean values
FALSE = "false"
TRUE = "true"


def custom_type(custom: str) -> str:
    """
    Custom integer type, the integer type cannot be less than 0 or more than 126.
    :param custom: str for integer type.
    :return: str for integer type.
    """

    if custom[0] not in ['u', 'i']:
        raise Exception("Not a basic type of integer, signed certificate 'i', unsigned integer 'u'.")
    if int(custom[1:]) not in list(range(1, 127)):
        raise Exception("The integer type cannot be less than 0 or more than 126.")

    return custom


def set_str(str_len):
    """
    Set string length to form string type
    :param str_len: str length
    :return: string type
    """

    return f"str{LESS_THAN}{str_len}{GREATER_THAN}"


def array_type(arr_type: str, arr_len: int or N) -> str:
    """
    Customer define array type
    :param arr_type:
    :param arr_len
    :return: str for array type.
    """

    if arr_type not in PRIMITIVE_TYPE and arr_type not in GENERICS:
        raise TypeError("Input \"type\" value is not a primitive type")

    return f"[{arr_type}; {arr_len}]"
