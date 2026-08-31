dict1 = {
    'a': 2,
    'b': 1,
    'c': 3,
    'd': 1
}

key = input("Enter the key you want to search:  ")

if key in dict1:
    print(f"Value is: {dict1[key]}")
else:
    print("The key is missing")