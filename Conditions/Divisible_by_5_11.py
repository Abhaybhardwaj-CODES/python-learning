n = int(input("Enter the number: "))
if(n % 5 ==0):
        print("The number is divisible by 5")
elif(n % 11 ==0):
        print("The number is divisible by 11")  
elif(n % 5 ==0 and n % 11 ==0):
        print("The number is divisible by both 5 and 11")
else:
        print("The number is not divisible by 5 or 11")                
