import csv
from pprint import pprint
# pprint = "Pretty Print" for nice to console
# python dictionary object is very helpful
# Has keys/values where values can be strings
# be sure to watch quotes 
EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

#Use "with" because will only leave file open briefly
# csv.DictReader is the type of file reader to use
# Then turn into a list so it will stay in memory
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
