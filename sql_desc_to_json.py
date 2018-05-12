"""
Converts `desc table_name` output to json

How?
Write the output of `desc table_name` command in mysql to a file (table_name.desc)

Run the command - `python script.py table_name.desc`
"""

import json
import sys

if len(sys.argv) != 2:
    print "No .desc file specified"
    exit()

try:
    f = open(sys.argv[1], 'r')
except:
    print "File "+sys.argv[1]+" not found"
    exit()

table_name = f.name.replace('.desc', '')

output = {}
output[table_name] = []
line_number = 0

ignore_lines = [0, 1, 2, 3]

file_length = 0
for line in f:
    file_length = file_length + 1
for ignore_line in range(4):
    ignore_lines.append(file_length)
    file_length = file_length - 1
f.close()

f = open(sys.argv[1], 'r')
for line in f:
    if line_number not in ignore_lines:
        count = 0
        column_name = ""
        for char in line:
            if count == 2:
                break
            if char == '|':
                count = count + 1
            elif char.isalpha() or char.isdigit() or char == '_':
                column_name = column_name + char
        output[table_name].append(column_name)
    line_number = line_number + 1
print json.dumps(output)
