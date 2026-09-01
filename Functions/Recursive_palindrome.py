def palin(args):
    if len(args) <= 1:
        return True
    else:
        if args[0] == args[-1]:
            return palin(args[1:-1])
        else:
            return False

        
n=input("Enter a string to check if it is a palindrome: ")
args = n.lower()  # Convert the input string to lowercase for case-insensitive comparison
if palin(args):
    print("The string is a palindrome.")        
else:
    print("The string is not a palindrome.")