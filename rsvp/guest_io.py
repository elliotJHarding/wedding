import csv

def import_guest_csv(file):
    with open(file) as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        for row in r:
            print(row)
