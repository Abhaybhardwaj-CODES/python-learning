Str = input("Enter a string: ")
og_str = Str
print(f"original string is:{Str}" )
Str_after_replacement = ""
for i in range(len(Str)):
       if Str[i] == 'a':
          Str_after_replacement  += 'A'
          
       else:
            Str_after_replacement += Str[i]
print(f"String after replacement is: {Str_after_replacement}")               
                              