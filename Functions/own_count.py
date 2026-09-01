def count(args):
    """Return the count of the given arguments."""
    count = args[0]
    for i in args:
        count += i


    return count

numbers = [17, 4, 29, 11, 42, 8, 35, 2, 19, 50, 7, 31, 14, 26, 3]
args = numbers
result = count(args)
print(result)