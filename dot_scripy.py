"""
If you're using csv tool kit's `in2csv` for converting xlsx to csv you might have faced an issue where
your integers have a `.0` appended in the csv, below script simply removes them and creates a fresh csv output
"""
import csv

with open('example.csv', 'rb') as f:
    reader = csv.reader(f)
    row_list = list(reader)

new_row_list = []
for row in row_list:
    new_row = []
    for r in row:
        new_r = ""
        if r.endswith(".0"):
            new_r = r[:-2]
        else:
            new_r = r
        new_row.append(new_r)
    new_row_list.append(new_row)

writer = csv.writer(open('example_output.csv', 'w'))
writer.writerows(new_row_list)
