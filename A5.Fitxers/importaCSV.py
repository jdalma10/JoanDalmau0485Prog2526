
import os
wd = os.getcwd()

import csv

with open(wd+'\JoanDalmau0485Prog2526\A5.Fitxers\data.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


