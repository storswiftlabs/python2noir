from .sign import LESS_THAN, GREATER_THAN

Int8 = 'i8'
Int16 = 'i16'
Int32 = 'i32'
Int64 = 'i64'
Int126 = 'i126'
Unt8 = 'u8'
Unt16 = 'u16'
Unt32 = 'u32'
Unt64 = 'u64'
Unt126 = 'u126'
FALSE = False
TRUE = True
FIELD = 'Field'


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
