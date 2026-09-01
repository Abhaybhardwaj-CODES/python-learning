def sq(n):
    return n * n
def cube(n):
    return n * n * n
def sum(n):
    return n + n

n = int(input("Enter a number: "))
print("Result:", sq(cube(sum(n))))