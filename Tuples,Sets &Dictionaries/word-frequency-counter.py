sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)