marks = {
    "Rahul": 78,
    "Aman": 92,
    "Priya": 65,
    "Neha": 88,
    "Karan": 71
}
l=list(marks)

l_duplicate = []

for i in range(len(l)):
    if l.count(l[i]) > 1 and l[i] not in l_duplicate:
        l_duplicate = l_duplicate + [l[i]]
    

result = dict(l_duplicate)
print(result)        