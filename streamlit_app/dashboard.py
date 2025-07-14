import streamlit as st
from utils import read_iocs_from_csv
from virustotal import check_ip

def main():
    st.title("IOC Detector Dashboard")
    st.write("عرض مؤشرات الاختراق والتحقق منها باستخدام VirusTotal")

    file_path = "data/sample_iocs.csv"
    iocs = read_iocs_from_csv(file_path)

    results = []
    for ip in iocs:
        result = check_ip(ip)
        results.append(result)

    for res in results:
        st.write(f"**IP:** {res['ip']}")
        if "error" in res:
            st.error(f"Error: {res['error']}")
        else:
            st.success(f"Malicious: {res['malicious']}, Suspicious: {res['suspicious']}")
        st.markdown("---")

if __name__ == "__main__":
    main()
