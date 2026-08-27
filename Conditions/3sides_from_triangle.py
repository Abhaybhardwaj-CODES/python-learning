Side_1 = int(input("Enter the first side of triangle: "))
Side_2 = int(input("Enter the second side of triangle: "))
Side_3 = int(input("Enter the third side of triangle: "))   

if (Side_1 + Side_2 > Side_3 and Side_2 + Side_3 > Side_1 and Side_1 + Side_3 > Side_2):
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")