n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(1, n + 1):
    for j in range(i):
        print(a, end=" ")
        a, b = b, a + b
    print(a)