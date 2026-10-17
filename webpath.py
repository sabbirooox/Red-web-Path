import requests
import threading
import os
import sys
import time

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install colorama requests")
    from colorama import Fore, Style, init
    init(autoreset=True)

target_url = ""
wordlist = ["admin", "login", "backup", "config", "robots.txt", "dashboard", "api", "uploads", "images", "test"]

def scan_path(path):
    global target_url
    url = f"{target_url}/{path}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(Fore.GREEN + f"[+] FOUND: {url} (Status: 200)")
        elif response.status_code == 403:
            print(Fore.YELLOW + f"[!] PROTECTED: {url} (Status: 403)")
        elif response.status_code == 301 or response.status_code == 302:
            print(Fore.CYAN + f"[*] REDIRECT: {url} (Status: {response.status_code})")
        else:
            print(Fore.RED + f"[-] NOT FOUND: {url} (Status: {response.status_code})")
    except requests.exceptions.RequestException:
        pass 

def start_scan():
    global target_url
    target_url = input(Fore.WHITE + "Enter Target URL (e.g., http://testphp.vulnweb.com): ").strip()
    if not target_url.startswith("http"): target_url = "http://" + target_url
    print(Fore.CYAN + f"\n[*] Scanning {target_url}...")
    print(Fore.RED + "--------------------------------------------------")
    threads = []
    for path in wordlist:
        t = threading.Thread(target=scan_path, args=(path,))
        threads.append(t)
        t.start()
    for thread in threads: thread.join()
    print(Fore.RED + "--------------------------------------------------")
    print(Fore.GREEN + "[+] Scan Complete!")
    input(Fore.YELLOW + "\nPress Enter to exit...")

# --- HOMEPAGE DESIGN ---
os.system('clear')
print(Fore.RED + "==================================================")
print(Fore.RED + Style.BRIGHT + "  ____  _____ ____    __        _____ ____  _   _  ____  _   _ ")
print(Fore.RED + Style.BRIGHT + " |  _ \| ____|  _ \   \ \      / /| ____|  _ \| | | ||  _ \| | | |")
print(Fore.RED + Style.BRIGHT + " | |_) |  _| | | | |   \ \ /\ / / |  _| | |_) | |_| || |_) | |_| |")
print(Fore.RED + Style.BRIGHT + " |  _ <| |___| |_| |    \ V  V /  | |___|  _ <|  _  ||  __/|  _  |")
print(Fore.RED + Style.BRIGHT + " |_| \_\_____|____/      \_/\_/   |_____|_| \_\_| |_||_|    |_| |_|")
print(Fore.RED + "==================================================")
print(Fore.MAGENTA + Style.BRIGHT + "                 DEVELOPER BY SABBIR ØX")
print(Fore.RED + "==================================================")
print("")

start_scan()
