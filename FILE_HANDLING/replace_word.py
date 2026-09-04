with open("f1.txt", "r") as f:
    content = f.read()
    for line in content.splitlines():
        if line == "Hello, World!":
            print("Found the line: Hello, World!")
            replace_line = "Hello, Python!"
            content = content.replace(line, replace_line)