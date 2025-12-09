
import csv

import os
wd = os.getcwd()
rows = [
    ["name", "age"],
    ["Alice", 30],
    ["Bob", 25],
]

with open(wd+'\JoanDalmau0485Prog2526\A5.Fitxers\output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(rows)








