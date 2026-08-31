words = ["apple", "ant", "ball", "banana", "cat", "car"]

groups = {}

for word in words:

    first_letter = word[0]

    if first_letter not in groups:
        groups[first_letter] = []

    groups[first_letter].append(word)

print("Grouped words:", groups)