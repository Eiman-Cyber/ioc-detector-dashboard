import streamlit as st
import pandas as pd
from virustotal import check_ip

def check_iocs(iocs):
    results = []
    for ip in iocs:
        res = check_ip(ip)
        results.append(res)
    return results

def main():
    st.title("IOC Detector Dashboard 📊")
    st.markdown("### ارفع ملف CSV يحتوي على IPs للفحص")

    uploaded_file = st.file_uploader("اختر ملف CSV", type=["csv"])

    if uploaded_file is not None:
        df_iocs = pd.read_csv(uploaded_file, header=None, names=["ip"])
        iocs = df_iocs["ip"].tolist()

        st.markdown(f"تم تحميل **{len(iocs)}** مؤشر اختراق ✅")

        with st.spinner("🔍 جاري فحص المؤشرات..."):
            results = check_iocs(iocs)

        for res in results:
            st.write(f"**IP:** {res['ip']}")
            if "error" in res:
                st.error(f"خطأ: {res['error']}")
            else:
                st.success(f"Malicious: {res['malicious']}, Suspicious: {res['suspicious']}")
            st.markdown("---")
    else:
        st.info("يرجى رفع ملف بصيغة CSV لبدء الفحص")

if __name__ == "__main__":
    main()

