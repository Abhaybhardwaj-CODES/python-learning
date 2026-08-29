Str = input("Enter the string: ")

compressed = ""
count = 1

for i in range(len(Str) - 1):
    if Str[i] == Str[i + 1]:
        count += 1
    else:
        compressed += Str[i] + str(count)
        count = 1

compressed += Str[-1] + str(count)

print("Compressed string:", compressed)