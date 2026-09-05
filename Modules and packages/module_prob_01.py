def valid_id(id_number):
    return len(id_number) == 10 and id_number.isdigit()
def valid_email(email):
    return "@" in email and "." in email and len(email) > 5