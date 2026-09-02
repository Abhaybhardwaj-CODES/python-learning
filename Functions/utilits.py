def vali_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return True
def vali_name(name):
    if len(name) < 3:
        raise ValueError("Name must be at least 3 characters long.")
    return True
def vali_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email must contain '@' and '.'")
    return True