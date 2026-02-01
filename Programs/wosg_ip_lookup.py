import os
import re
import json
import urllib.request
from ipaddress import ip_address
from colorama import init

init(autoreset=True)

# Yellow -> Dark Red gradient
GRADIENT = [
    "\033[38;2;255;255;0m",
    "\033[38;2;255;200;0m",
    "\033[38;2;255;165;0m",
    "\033[38;2;255;120;0m",
    "\033[38;2;220;60;0m",
    "\033[38;2;139;0;0m",
    "\033[0m"
]

def gradient_text(text):
    result = ""
    length = len(text)
    steps = len(GRADIENT) - 1
    for i, c in enumerate(text):
        idx = int(i / max(length, 1) * steps)
        result += GRADIENT[idx] + c
    return result + GRADIENT[-1]

BANNER = r"""
 █     █░      ▒█████         ██████        ▄████ 
▓█░ █ ░█░     ▒██▒  ██▒     ▒██    ▒       ██▒ ▀█▒
▒█░ █ ░█      ▒██░  ██▒     ░ ▓██▄        ▒██░▄▄▄░
░█░ █ ░█      ▒██   ██░       ▒   ██▒     ░▓█  ██▓
░░██▒██▓  ██▓ ░ ████▓▒░ ██▓ ▒██████▒▒ ██▓ ░▒▓███▀▒
░ ▓░▒ ▒   ▒▓▒ ░ ▒░▒░▒░  ▒▓▒ ▒ ▒▓▒ ▒ ░ ▒▓▒  ░▒   ▒ 
  ▒ ░ ░   ░▒    ░ ▒ ▒░  ░▒  ░ ░▒  ░ ░ ░▒    ░   ░ 
  ░   ░   ░   ░ ░ ░ ▒   ░   ░  ░  ░   ░   ░ ░   ░ 
    ░      ░      ░ ░    ░        ░    ░        ░ 
                                                    V2
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def valid_ip(ip):
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False

def geo_lookup(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,hosting"
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read().decode())

def risk_assessment(ip, geo):
    risk = {
        "private_or_reserved": ip_address(ip).is_private,
        "proxy_detected": geo.get("proxy"),
        "hosting_provider": geo.get("hosting"),
        "vpn_or_datacenter_likelihood": False,
        "risk_level": "Low"
    }

    score = 0

    if risk["private_or_reserved"]:
        score += 2
    if risk["proxy_detected"]:
        score += 3
    if risk["hosting_provider"]:
        score += 3

    if score >= 6:
        risk["risk_level"] = "High"
    elif score >= 3:
        risk["risk_level"] = "Medium"

    return risk

def main():
    clear()
    print(gradient_text(BANNER))

    ip = input(gradient_text("\n[+] Enter IP address: "))

    if not valid_ip(ip):
        print(gradient_text("\n[-] Invalid IP address"))
        return

    print(gradient_text("\n[+] Running geolocation lookup...\n"))
    geo = geo_lookup(ip)

    if geo.get("status") != "success":
        print(gradient_text(f"Lookup failed: {geo.get('message')}"))
        return

    geo_output = f"""
IP Address : {ip}
Country    : {geo.get('country')}
Region     : {geo.get('regionName')}
City       : {geo.get('city')}
ZIP        : {geo.get('zip')}
Latitude   : {geo.get('lat')}
Longitude  : {geo.get('lon')}
Timezone   : {geo.get('timezone')}
ISP        : {geo.get('isp')}
Org        : {geo.get('org')}
ASN        : {geo.get('as')}
Proxy      : {geo.get('proxy')}
Hosting    : {geo.get('hosting')}
"""
    print(gradient_text(geo_output))

    choice = input(gradient_text("\n[?] Run IP risk analysis? (Y/N): ")).lower()

    if choice == "y":
        print(gradient_text("\n[+] Running risk analysis...\n"))
        risk = risk_assessment(ip, geo)

        risk_output = f"""
Private / Reserved : {risk['private_or_reserved']}
Proxy Detected     : {risk['proxy_detected']}
Hosting Provider   : {risk['hosting_provider']}
Risk Level         : {risk['risk_level']}
"""
        print(gradient_text(risk_output))
    else:
        os.system("python wosg_v2.py")

if __name__ == "__main__":
    main()
