Int3 = 'i3'
Int5 = 'i5'
Int8 = 'i8'
Int16 = 'i16'
Int32 = 'i32'
Int64 = 'i64'
Int126 = 'i126'
Unt3 = 'u3'
Unt5 = 'u5'
Unt8 = 'u8'
Unt16 = 'u16'
Unt32 = 'u32'
Unt64 = 'u64'
Unt126 = 'u126'
FALSE = False
TRUE = True
STR = 'str'
FIELD = 'Field'


def custom_type(self, custom: str) -> str:
    sign = custom[0]
    size = custom[1:]
    assert sign in ['u', 'i']
    assert size in list(range(1, 127))
    return custom
