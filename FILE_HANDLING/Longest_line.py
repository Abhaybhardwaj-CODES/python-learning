with open("f1.txt", "r") as f:
    content = f.read()
    for lines in f:
        longest_line = max(lines, key=len)