Str = input("Enter a string: ")

str_after_removing_duplicates = ""
for i in range(len(Str)):
    if Str[i] not in str_after_removing_duplicates:
        str_after_removing_duplicates = str_after_removing_duplicates + Str[i]
    
print("The string after removing duplicates is:", str_after_removing_duplicates)