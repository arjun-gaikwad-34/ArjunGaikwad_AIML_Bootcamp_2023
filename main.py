cities = ["New York", "Washington","London","Moscow"]
cities.sort()
maximum = -1;
for i in cities:
    if len(i) > maximum:
        maximum = len(i)

for i in cities:
    if len(i) > len(i+1):
        print(i)

