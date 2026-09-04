N = input("Enter a character to search: ")

with open("f1.txt", "r") as f:
    content = f.read()

    found = False

    for l in content:
        if l == N:
            found = True
            break

    if found:
        print("Found the character:", N)
    else:
        print("Character not found.")