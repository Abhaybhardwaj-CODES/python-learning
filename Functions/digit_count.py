def digit_count(arg):
    """Return the length of the given argument."""
    count = 0
    for _ in arg:
        count += 1
    return count

args = numbers = [17, 4, 29, 11, 42, 8, 35, 2, 19, 50, 7, 31, 14, 26, 3]
result = digit_count(args)
print(result)