from collections import defaultdict
d = defaultdict(list)
file="C:/Users/Skrillex/Downloads/country-citis.csv"
with open(file) as data:
        for line in data:
            Country,City = line.strip("\n").split(',')
            d[Country].append(City)

print(d)
