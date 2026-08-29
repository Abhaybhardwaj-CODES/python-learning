l = [12, 5, 8, 12, 3, 7, 5, 10, 3, 15]

for i in range(len(l)):
    count = 0

    for j in range(len(l)):
        if l[i] == l[j]:
            count += 1

    if count == 1:
        print("Unique element:", l[i])
        