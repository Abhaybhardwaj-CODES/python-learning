marks = {
    "Rahul": 78,
    "Aman": 92,
    "Priya": 65,
    "Neha": 88,
    "Karan": 71
}

names = list(marks)

for i in range(len(names)):
    for j in range(i+1 , len(names)):
           if marks[names[i]] < marks[names[j]]:
            names[i], names[j] = names[j], names[i]
for name in names:
    print(f"Your name: {name}, {marks[name]}")            
