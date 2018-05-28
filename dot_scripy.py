"""
If you're using csv tool kit's `in2csv` for converting xlsx to csv you might have faced an issue where
your integers have a `.0` appended in the csv, below script simply removes them and creates a fresh csv output
"""
import csv

with open('example.csv', 'rb') as f:
    reader = csv.reader(f)
    price_list = list(reader)

new_price_list = []
for price in price_list:
    new_price = []
    for p in price:
        new_p = ""
        if p.endswith(".0"):
            new_p = p[:-2]
        else:
            new_p = p
        new_price.append(new_p)
    new_price_list.append(new_price)

writer = csv.writer(open('example_output.csv', 'w'))
writer.writerows(new_price_list)
