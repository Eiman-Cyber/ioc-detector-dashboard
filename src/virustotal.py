import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()  # يحمل المتغيرات من ملف .env

API_KEY = os.getenv("VT_API_KEY")

def check_ip(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        return {
            "ip": ip,
            "malicious": malicious,
            "suspicious": suspicious
        }
    elif response.status_code == 429:
        print("Rate limit exceeded. Waiting...")
        time.sleep(15)
        return check_ip(ip)
    else:
        print(f"Error for {ip}: {response.status_code}")
        return {"ip": ip, "error": response.status_code}
