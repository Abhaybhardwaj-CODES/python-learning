

l = [1, 2, 3, 4, 5]

first = l[0]

for i in range(len(l) - 1):
    l[i] = l[i + 1]

l[-1] = first

print(l)