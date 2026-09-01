def sum(args):
    """Return the sum of the given arguments."""
    total = 0
    for num in args:
        total += num
    return total
args = [2,9,8,76,53]
result = sum(args)
print(result)