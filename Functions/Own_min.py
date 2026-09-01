def min (*args):
    """Return the minimum value from the given arguments."""
    if not args:
        raise ValueError("min() arg is an empty sequence")

    minimum = args[0]
    for num in args[1:]:
        if num < minimum:
            minimum = num
    return minimum


args = [3, 5, 2, 8, 1]
result = min(*args)
print(result)