l1 = [12, 5, 8, 12, 3, 7, 5, 10, 3, 15]
l2 = [8, 4, 15, 6, 3, 12, 9, 5, 4, 18]
union_list = []

for i in range(len(l1)):
   if l1[i] not in union_list:
      union_list = union_list +[ l1[i]]

for j in range(len(l2)):
   if l2[j] not in  union_list:
      union_list = union_list + [l2[j]]

print(f"The union list is: {union_list}")      