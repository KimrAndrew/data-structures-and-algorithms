from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_all():
    assert validate_brackets('()[[EXTRA CHARACTERS]])')
    assert validate_brackets(f'{{}}')
    assert validate_brackets(f'{{}}(){{}}')
    assert validate_brackets(f'(){{}}[[]]')
    assert validate_brackets(f'{{}}{{Code}}[Fellows](())')
    assert not validate_brackets(f'[({{}}]')
    assert not validate_brackets(f'[({{}}]')
    assert not validate_brackets('(](')
    assert not validate_brackets(f'{{(}})')
    assert not validate_brackets('][')