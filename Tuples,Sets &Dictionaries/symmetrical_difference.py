s = (1,2,3,1,4,6,7,3,8,9)
s1 = (1,2,3,4,2,4,65,)
symmetric_set = set()
for i in s:
    if i not in s1:
        symmetric_set.add(i)
for j in s:
    if j not in s:
        symmetric_set.add(j)
print(f"The symmetric element  set is: {symmetric_set}")        