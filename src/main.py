from utils import read_iocs_from_csv

def main():
    file_path = "data/sample_iocs.csv"
    iocs = read_iocs_from_csv(file_path)
    print("IOCs read from CSV:")
    for ioc in iocs:
        print(ioc)

if __name__ == "__main__":
    main()
