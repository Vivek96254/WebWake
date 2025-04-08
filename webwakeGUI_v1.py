import customtkinter as ctk
import threading
import requests
import time
from win11toast import toast

# Settings
ctk.set_appearance_mode("Dark")  # "Light" or "System"
ctk.set_default_color_theme("blue")

running = False

def ping_website():
    global running
    url = url_entry.get()
    try:
        interval = int(interval_entry.get())
    except ValueError:
        log("⛔ Interval must be a number")
        return
    if not url.startswith("http"):
        log("⛔ URL must start with http or https")
        return

    while running:
        try:
            res = requests.get(url, headers={"User-Agent": "PingApp"})
            toast("Pinged", f"{url} → Status {res.status_code}")
            log(f"✅ {url} → {res.status_code}")
        except Exception as e:
            toast("Error", str(e))
            log(f"❌ Error: {e}")
        time.sleep(interval * 60)

def start():
    global running
    if not running:
        running = True
        log("🚀 Started pinging...")
        threading.Thread(target=ping_website, daemon=True).start()

def stop():
    global running
    running = False
    log("⏹️ Stopped.")

def log(msg):
    output_box.insert("end", msg + "\n")
    output_box.see("end")

# UI
app = ctk.CTk()
app.title("🛰️ WebWake")
app.geometry("500x400")

title = ctk.CTkLabel(app, text="🌐 Website Pinger", font=("Arial", 20))
title.pack(pady=10)

url_entry = ctk.CTkEntry(app, placeholder_text="Enter website URL", width=400)
url_entry.insert(0, "https://myportfolio-1ovu.onrender.com/")
url_entry.pack(pady=5)

interval_entry = ctk.CTkEntry(app, placeholder_text="Interval in minutes", width=400)
interval_entry.insert(0, "14")
interval_entry.pack(pady=5)

btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

start_btn = ctk.CTkButton(btn_frame, text="Start", command=start, width=150)
start_btn.pack(side="left", padx=10)

stop_btn = ctk.CTkButton(btn_frame, text="Stop", command=stop, width=150)
stop_btn.pack(side="left", padx=10)

output_box = ctk.CTkTextbox(app, width=460, height=200)
output_box.pack(pady=10)

app.mainloop()
