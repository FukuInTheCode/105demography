import csv
import sys


def get_data(abrs: list[str]) -> list[list[str]]:
    listData = []

    with open('assets/105demography_data.csv', 'r') as csvfile:
        content = csv.reader(csvfile, delimiter=';')
        header = next(content)
        abrs_index = header.index('Country Code')
        for row in content:
            if row[abrs_index] in abrs:
                listData.append(row)
        if len(listData) != len(abrs):
            sys.exit(84)
    return listData
