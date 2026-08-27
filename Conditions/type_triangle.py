a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

if a==b and b==c:
    print("The triangle is equilateral.")
elif a==b or b==c or a==c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")