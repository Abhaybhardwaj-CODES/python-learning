def max (*args):
    """Return the maximum value from the given arguments."""
    if not args:
        raise ValueError("max() arg is an empty sequence")
    
    maximum = args[0]
    for num in args[1:]:
        if num > maximum:
            maximum = num
    return maximum


args = [3, 5, 2, 8, 1]
result = max(*args)
print(result)
