l1 =  [1,2,3,4,5,6,7,9]
t1 = ()
for i in range(len(l1)):
    if l1[i] not in t1:
        t1 = t1 + (l1[i],)
print(f"The list is converted to tuple: {t1}")        
