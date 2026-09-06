import re

pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"

def is_valid_email(email):
    return bool(re.match(pattern, email))

print(is_valid_email("john.doe@example.com"))   # True
print(is_valid_email("bad-email@@x"))            # False