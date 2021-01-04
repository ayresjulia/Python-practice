def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) % 2 == 0:
        if parens[0] is not ")" or parens[len(parens)-1] is not "(":
            return True
        else:
            return False
    return False

# Solution #2:
# count = 0

#     for p in parens:
#         if p == '(':
#             count += 1
#         elif p == ')':
#             count -= 1

#         # fast fail: too many right parens
#         if count < 0:
#             return False

#     return count == 0
