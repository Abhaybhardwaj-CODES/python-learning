l = [1, 5, 3, 5, 2, 1, 8, 3, 5, 2]

l_duplicate = []

for i in range(len(l)):
    if l.count(l[i]) > 1 and l[i] not in l_duplicate:
        l_duplicate = l_duplicate + [l[i]]

print(f"The duplicate numbers are: {l_duplicate}")