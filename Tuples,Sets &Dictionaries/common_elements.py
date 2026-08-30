s = (1,2,3,1,4,6,7,3,8,9)
s1 = (1,2,3,4,2,4,65,)
print(f"the original set is: {s}")
common_elements = set()


for i  in s:
   for j in s1:
     if  i == j:
         common_elements.add(i)  
print(f"The common elements: {common_elements}")            

    
            