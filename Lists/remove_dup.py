l = [1, 5, 3, 5, 2, 1, 8, 3, 5, 2]
l_without_duplicate =[l[0]]
for i in range (len(l)):
    if l[i] not in l_without_duplicate:
        l_without_duplicate = l_without_duplicate + [l[i]]
print(f"The List without Duplicate is: {l_without_duplicate}")        