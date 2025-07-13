from utils import read_iocs_from_csv
from virustotal import check_ip

def main():
    file_path = "data/sample_iocs.csv"
    iocs = read_iocs_from_csv(file_path)

    print("Checking IOCs with VirusTotal...\n")
    for ip in iocs:
        result = check_ip(ip)
        print(f"IP: {result['ip']}")
        if "error" in result:
            print(f" ❌ Error: {result['error']}")
        else:
            print(f" 🔴 Malicious: {result['malicious']}, 🟠 Suspicious: {result['suspicious']}")
        print("-" * 30)

if __name__ == "__main__":
    main()
