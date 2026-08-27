sub_1 = int(input("Enter marks for subject 1: "))
sub_2 = int(input("Enter marks for subject 2: "))
sub_3 = int(input("Enter marks for subject 3: "))

total_marks = sub_1 + sub_2 + sub_3
average_marks = total_marks / 3

if average_marks >= 90:
    print("Grade: A+")
elif average_marks >= 80:
    print("Grade: A")       
elif average_marks >= 70:
    print("Grade: B")   
elif average_marks >= 60:
    print("Grade: C")
elif average_marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")