l = [1,1,1,1,4,1,5,225,5,2]
for i in range (len(l)):
    count = 0
    for j in range (len(l)):
        if l[i]==l[j]:
            count = count +1 
    print(f"The frequency of numbers: {l[i]} in list are: {count}")