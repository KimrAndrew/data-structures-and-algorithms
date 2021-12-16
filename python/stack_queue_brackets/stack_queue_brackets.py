from stack_and_queue.stack_and_queue import Stack

OPENING_CHARS = ( '{' , '[' , '(' )
CLOSING_CHARS = ( '}' , ']' , ')' )

MATCHED_CHARS = {
'{' : '}',
'[' : ']',
'(' : ')'
}

def push_chars_to_stack(String: str) -> Stack:
    stacked_chars = Stack()
    for char in String:
       if char in OPENING_CHARS or char in CLOSING_CHARS:
            stacked_chars.push(char)
    return stacked_chars

def recursive_validate(unchecked_stack: Stack,checked_stack: Stack) -> bool:
    if unchecked_stack.is_empty():
        return True
    elif unchecked_stack.peek() in CLOSING_CHARS:
            checked_stack.push(unchecked_stack.pop())
            return recursive_validate(unchecked_stack,checked_stack)
    # # only an issue when invalid brackets
    # # just makes sure recursion doesn't break
    elif checked_stack.is_empty():
        checked_stack.push(unchecked_stack.pop())
    else:
        if MATCHED_CHARS[unchecked_stack.peek()] == checked_stack.peek():
            unchecked_stack.pop()
            checked_stack.pop()
            return recursive_validate(unchecked_stack,checked_stack)
        else:
            return False

def validate_brackets(String: str) -> bool:
    unchecked_stack = push_chars_to_stack(String)
    checked_stack = Stack()
    return recursive_validate(unchecked_stack,checked_stack)