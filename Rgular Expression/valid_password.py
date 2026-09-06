import re  

def password_report(pwd):
         checks = {
        "length": bool(re.search(r".{10,}", pwd)),
        "lowercase": bool(re.search(r"[a-z]", pwd)),
        "uppercase": bool(re.search(r"[A-Z]", pwd)),
        "digit": bool(re.search(r"\d", pwd)),
        "special": bool(re.search(r"[^\w\s]", pwd)),
        "no_common_pattern": not bool(re.search(r"(1234|password|qwerty)", pwd, re.IGNORECASE))}

         score = sum(checks.values())
         return checks, score

report, score = password_report("MyP@ssw0rd123")
print(report, score)