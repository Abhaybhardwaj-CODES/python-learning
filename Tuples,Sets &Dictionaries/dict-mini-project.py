cache = {
    "apple": 120,
    "banana": 60,
    "mango": 150,
    "orange": 80,
    "grapes": 100
}  

key = input("Enter the fruiit name: ")

if key in cache:
    print(f"The value is found: {cache[key]}")
else:
    value = input("Enter the value: ")
    cache[key] = value
    print(f"The value is stored in cache: {value}") 
print(f"Cache: {cache}")    