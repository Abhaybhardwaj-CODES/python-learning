def greet(name):
    return f"Hello, {name}"

# Assign to a variable
say_hi = greet
print(say_hi("Alice"))          # "Hello, Alice"

# Store in a data structure
funcs = [greet, str.upper, len]

# Pass as an argument
def apply(func, value):
    return func(value)
print(apply(greet, "Bob"))      # "Hello, Bob"

# Return from another function
def get_greeter():
    return greet
print(get_greeter()("Carl"))    # "Hello, Carl"

# Have attributes
greet.custom_attr = "info"
print(greet.custom_attr)