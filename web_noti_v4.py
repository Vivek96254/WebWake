import time
import threading
import requests
from win11toast import toast

url = "https://example.com"
interval = 14 * 60  # 14 minutes

def open_website_silently():
    while True:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
            response = requests.get(url, headers=headers)
            status = response.status_code
            toast("Website Visited", f"{url} returned status {status}")
        except Exception as e:
            toast("Visit Failed", f"Error: {str(e)}")

        time.sleep(interval)

# Start background thread
threading.Thread(target=open_website_silently, daemon=True).start()

# Keep script alive
while True:
    time.sleep(1)
