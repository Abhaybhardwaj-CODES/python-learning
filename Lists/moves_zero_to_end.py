l = [4, 0, 7, 0, 2, 9, 0, 5]
count = 0
new_list = []
for i in range (len(l)):
    if l[i] == 0:
        count = count + 1
    else:
        new_list = new_list + [l[i]]
for i in range(count):
    new_list = new_list + [0]


print(new_list)    