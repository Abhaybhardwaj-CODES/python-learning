a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print(f"The middle number is: {a}")
elif (b >= a and b <= c) or (b <= a and b >= c):
    print(f"The middle number is: {b}")
else:
    print(f"The middle number is: {c}")