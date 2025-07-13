import csv

def read_iocs_from_csv(file_path):
    iocs = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            iocs.append(row['ioc'])
    return iocs
