l1 = [12, 5, 8, 12, 3, 7, 5, 10, 3, 15]
l2 = [8, 4, 15, 6, 3, 12, 9, 5, 4, 18]
intersection_list = []

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            intersection_list = l1[i] 
print(f"The intersection list is:{intersection_list}")   
    
