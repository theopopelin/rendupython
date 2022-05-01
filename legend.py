import csv

f = open (r"C:\Users\nexus\Downloads\cars.csv")
reader = csv.reader(f)
for row in reader:
    print(row[0].split(";")[5])

