from transpiler.sub_module.sign import get_sign4bool


def is_bool_expression(expression: str):
    # Inspection the expression is a bool expression
    for sign in get_sign4bool():
        if sign in expression:
            return True
    # FIXME: Inspection process too easy.
    return False
