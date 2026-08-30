l = [1,45,89,6,4,7,]
target_sum = 95
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == target_sum:
            print(f"The pair of given sum {target_sum} is {l[i]} : {l[j]}")