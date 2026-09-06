class Validator:
    @staticmethod
    def valid_id(id_number):
        return len(id_number) == 10 and id_number.isdigit()

    @staticmethod
    def valid_email(email):
        return "@" in email and "." in email and len(email) > 5

    @staticmethod
    def valid_phone(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit() and phone_number[0] in "6789"

    @staticmethod
    def valid_password(password):
        return (len(password) >= 8
                and any(char.isdigit() for char in password)
                and any(char.isupper() for char in password)
                and any(char.islower() for char in password)
                and any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in password))


class StringValidator:
    @staticmethod
    def valid_string(s):
        return s.isalpha() and len(s) > 0


class NumberValidator:
    @staticmethod
    def valid_number(n):
        return n.isdigit() and len(n) > 0


