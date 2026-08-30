l = [1, 2, 3, 4, 5]

last = l[-1]

for i in range(len(l) - 1, 0, -1):
    l[i] = l[i - 1]

l[0] = last

print(l)