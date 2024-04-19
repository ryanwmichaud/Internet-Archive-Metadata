"""
Program for pulling metadata from each item in an Internet Archive collection
Ryan Michaud 4/17/2024 
"""

import internetarchive as ia
import csv

collection_identifier = 'collection:oberlinconservatorylibrary'
search = ia.search_items(collection_identifier)

#get a list of each field that appears in the collection
print("processings items...")
fields = []

for result in search:
    item = ia.get_item(result['identifier'])
    for field in item.metadata.keys():
        if field not in fields:
            fields.append(field)


#put title in first column and identifier in second
fields[0:2] = reversed(fields[0:2])

i = fields.index('title')    
temp = fields[0]
fields[0] = fields[i]
fields[i] = temp

#write csv
print("writing data to csv")
with open('metadata.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for result in search:
        item = ia.get_item(result['identifier'])
        row = item.metadata
        writer.writerow(row)

