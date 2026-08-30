s = (1,2,3,1,4,6,7,3,8,9)
print(f"the original set is: {s}")
without_dup_s1 = set()


for i  in s:
    if s[i] not in without_dup_s1:
        without_dup_s1.add(i)
print(f"the set without the duplicate is : {without_dup_s1}")        
