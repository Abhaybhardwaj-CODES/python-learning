with open("f1.txt", "r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)
    print(f"Total number of words in the file: {word_count}")