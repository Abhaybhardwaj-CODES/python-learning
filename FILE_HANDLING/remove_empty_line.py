with open("f1.txt", "r") as f:
    content = f.read()
    print(content)
    for line in content.splitlines():
        if line.strip() == "":
            print("Found an empty line.")
            content = content.replace(line, "")