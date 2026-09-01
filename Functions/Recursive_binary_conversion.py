def binary(n):
    if n == 0:
        print(0, end='')
    else:
        if n > 1:
            binary(n // 2)
        print(n % 2, end='')

n = int(input("Enter a decimal number: "))
print("Binary representation of", n, "is: ", end='')        