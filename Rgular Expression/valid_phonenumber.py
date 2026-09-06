import re
pattern = re.compile(r"""
    ^(?:\+?(?P<country>\d{1,3}))?      # optional country code
    [-.\s]?
    \(?(?P<area>\d{3})\)?               # area code
    [-.\s]?
    (?P<exchange>\d{3})                 # exchange
    [-.\s]?
    (?P<line>\d{4})$                    # line number
""", re.VERBOSE)

m = pattern.match("+91 (987) 654-3210")
if m:
    print(m.groupdict())
    # {'country': '91', 'area': '987', 'exchange': '654', 'line': '3210'}