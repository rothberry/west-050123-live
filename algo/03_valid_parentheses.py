""" 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

"""


def is_valid(s):
    # ? First
    # ! stretch case if s.length is odd, then it's automatically false
    # create an output Stack (or just a list acting as a stack)
    # iterate over the length of the str
    #   if the current value is an opening
    #     add to the stack
    #   if it's a closing
    #     check if the top of the stack is a matching parentheses
    #       if so, remove the top of the stack
    #       if not, break and return false
    # if the stack is empty, return true, else, return false

    if len(s) % 2 == 1:
        return False

    stack = []

    for p in s:
        if p in ["(", "{", "["]:
            stack.append(p)
        elif p == "}":
            if stack.pop() != "{":
                return False
        elif p == "]":
            if stack.pop() != "[":
                return False
        elif p == ")":
            if stack.pop() != "(":
                return False
        print(stack)
    return len(stack) == 0


print(is_valid("("))
print(is_valid("()"))
print(is_valid("(]"))
print(is_valid("({})"))
print(is_valid("({(((((((((((((((((((((((((())))))))))))))))))))))))))})"))
print(is_valid("({])"))
