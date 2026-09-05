import csv
with open("csv.f1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["abhay", "25", "male"])
    print("Data written to csv.f1.csv successfully.")