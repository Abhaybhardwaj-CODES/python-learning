def str_reverse(s):
    """Recursively reverse a string."""
    if len(s) == 0:
        return s
    else:
        return s[-1] + str_reverse(s[:-1])
s = "Hello, World!"
result = str_reverse(s)    