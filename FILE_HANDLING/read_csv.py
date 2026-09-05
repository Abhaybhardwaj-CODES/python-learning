import csv
with open("csv.f1.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)