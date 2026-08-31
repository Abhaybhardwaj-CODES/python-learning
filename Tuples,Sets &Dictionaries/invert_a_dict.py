marks = {
    "Rahul": 78,
    "Aman": 92,
    "Priya": 65
}

inverted = {}

for key in marks:
    inverted[marks[key]] = key

print(inverted)