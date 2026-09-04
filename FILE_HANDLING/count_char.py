with open("f1.txt", "r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)
    char_count = len(content)
    print(f"Total number of words in the file: {word_count}")
    print(f"Total number of characters in the file: {char_count}")