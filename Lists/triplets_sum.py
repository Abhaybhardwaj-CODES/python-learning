l = [1,45,89,6,4,7,]
target_sum = 99
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):

         if l[i] + l[j] +l[k] == target_sum:
            print(f"The triplets of given sum {target_sum} is {l[i]} : {l[j]} : {l[k]}")