import re
import json
from datetime import datetime

# ANSI escape codes for yellow-to-dark-red gradient
GRADIENT = [
    "\033[38;2;255;255;0m",   # Yellow
    "\033[38;2;255;200;0m",   # Yellow-Orange
    "\033[38;2;255;165;0m",   # Orange
    "\033[38;2;255;120;0m",   # Orange-Red
    "\033[38;2;220;60;0m",    # Red
    "\033[38;2;139;0;0m",     # Dark Red
    "\033[0m"                 # Reset
]

def gradient_text(text):
    """Apply gradient color to a string"""
    result = ""
    length = len(text)
    steps = len(GRADIENT) - 1
    for i, c in enumerate(text):
        color_index = int(i / length * steps)
        result += GRADIENT[color_index] + c
    result += GRADIENT[-1]
    return result

def print_gradient(text):
    """Print gradient-colored text"""
    print(gradient_text(text))

def input_gradient(prompt):
    """Input prompt with gradient"""
    return input(gradient_text(prompt))

def banner():
    banner_text = r"""
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

                        WINDOWS ONLY FOR RN     
                   https://discord.gg/m4Jc2Mj9Fy
                                               
"""
    print_gradient(banner_text)

def continent_from_country(country):
    continents = {
        "United States/Canada": "North America",
        "United Kingdom": "Europe",
        "Germany": "Europe",
        "France": "Europe",
        "India": "Asia",
        "Japan": "Asia",
        "Australia": "Oceania",
        "Russia": "Europe/Asia",
        "Italy": "Europe",
        "Brazil": "South America",
        "China": "Asia",
        "South Africa": "Africa",
        "Spain": "Europe",
        "Sweden": "Europe",
        "Netherlands": "Europe",
        "New Zealand": "Oceania",
        "South Korea": "Asia",
        "Portugal": "Europe",
        "Finland": "Europe",
        "Czech Republic": "Europe",
        "Ukraine": "Europe",
        "Poland": "Europe",
        "Switzerland": "Europe",
        "Austria": "Europe",
        "Egypt": "Africa",
        "Palestine": "Asia",
    }
    return continents.get(country, "Unknown")

def country_lat_lon_timezone(country):
    country_info = {
        "United States/Canada": ("37.0902", "-95.7129", "America/New_York"),
        "United Kingdom": ("55.3781", "-3.4360", "Europe/London"),
        "Germany": ("51.1657", "10.4515", "Europe/Berlin"),
        "France": ("46.2276", "2.2137", "Europe/Paris"),
        "India": ("20.5937", "78.9629", "Asia/Kolkata"),
        "Japan": ("36.2048", "138.2529", "Asia/Tokyo"),
        "Australia": ("-25.2744", "133.7751", "Australia/Sydney"),
        "Russia": ("61.5240", "105.3188", "Europe/Moscow"),
        "Italy": ("41.8719", "12.5674", "Europe/Rome"),
        "Brazil": ("-14.2350", "-51.9253", "America/Sao_Paulo"),
        "China": ("35.8617", "104.1954", "Asia/Shanghai"),
        "South Africa": ("-30.5595", "22.9375", "Africa/Johannesburg"),
        "Spain": ("40.4637", "-3.7492", "Europe/Madrid"),
        "Sweden": ("60.1282", "18.6435", "Europe/Stockholm"),
        "Netherlands": ("52.1326", "5.2913", "Europe/Amsterdam"),
        "New Zealand": ("-40.9006", "174.8860", "Pacific/Auckland"),
        "South Korea": ("35.9078", "127.7669", "Asia/Seoul"),
        "Portugal": ("39.3999", "-8.2245", "Europe/Lisbon"),
        "Finland": ("61.9241", "25.7482", "Europe/Helsinki"),
        "Czech Republic": ("49.8175", "15.4730", "Europe/Prague"),
        "Mexico": ("23.6345", "-102.5528", "America/Mexico_City"),
        "Argentina": ("-38.4161", "-63.6167", "America/Argentina/Buenos_Aires"),
        "Norway": ("60.4720", "8.4689", "Europe/Oslo"),
        "Belgium": ("50.5039", "4.4699", "Europe/Brussels"),
        "Switzerland": ("46.8182", "8.2275", "Europe/Zurich"),
        "Turkey": ("38.9637", "35.2433", "Europe/Istanbul"),
        "Egypt": ("26.8206", "30.8025", "Africa/Cairo")
    }
    return country_info.get(country, ("Unknown", "Unknown", "Unknown"))

def phone_lookup(phone):
    # Map country codes
    country_codes = {
        "1": "United States/Canada",
        "44": "United Kingdom",
        "49": "Germany",
        "33": "France",
        "91": "India",
        "81": "Japan",
        "61": "Australia",
        "7": "Russia",
        "39": "Italy",
        "55": "Brazil",
        "86": "China",
        "27": "South Africa",
        "34": "Spain",
        "46": "Sweden",
        "31": "Netherlands",
        "64": "New Zealand",
        "82": "South Korea",
        "351": "Portugal",
        "358": "Finland",
        "420": "Czech Republic",
        "380": "Ukraine",
        "48": "Poland",
        "41": "Switzerland",
        "43": "Austria",
        "20": "Egypt",
        "970": "Palestine",
    }

    phonersp = {
        "query": phone,
        "numberValid": False,
        "numberType": "Unknown",
        "numberAreaCode": "Unknown",
        "carrier": "Unknown",
        "continent": "Unknown",
        "countryName": "Unknown",
        "lat": "Unknown",
        "lon": "Unknown",
        "timezone": "Unknown"
    }

    # Clean phone number
    phone_clean = re.sub(r"[^\d+]", "", phone)
    if phone_clean.startswith("+"):
        phone_clean = phone_clean[1:]

    # Detect country code
    country_code = None
    for code in sorted(country_codes.keys(), key=lambda x: -len(x)):
        if phone_clean.startswith(code):
            country_code = code
            break

    if country_code:
        phonersp["numberValid"] = True
        phonersp["countryName"] = country_codes[country_code]
        phonersp["continent"] = continent_from_country(phonersp["countryName"])
        phonersp["numberAreaCode"] = phone_clean[len(country_code):len(country_code)+3] if len(phone_clean) > len(country_code)+3 else "Unknown"
        phonersp["numberType"] = "Mobile" if phonersp["numberAreaCode"].startswith("9") else "Landline"
        phonersp["carrier"] = "Unknown"

        lat, lon, timezone = country_lat_lon_timezone(phonersp["countryName"])
        phonersp["lat"] = lat
        phonersp["lon"] = lon
        phonersp["timezone"] = timezone

    phoneresults = f"\nPhone Number: {phonersp['query']}"\
                    f"\nExists: {phonersp['numberValid']}"\
                    f"\nPhone Number Type: {phonersp['numberType']}"\
                    f"\nArea Code: {phonersp['numberAreaCode']}"\
                    f"\nProvider: {phonersp['carrier']}"\
                    f"\nContinent: {phonersp['continent']}"\
                    f"\nCountry: {phonersp['countryName']}"\
                    f"\nLatitude(not consistent): {phonersp['lat']}"\
                    f"\nLongitude(not consistent): {phonersp['lon']}"\
                    f"\nTimezone: {phonersp['timezone']}"

    # Print with gradient
    print_gradient(phoneresults)

def main():
    banner()
    while True:
        phone = input_gradient("[+] Enter phone number (or type 'exit'): ")
        if phone.lower() == "exit":
            break
        phone_lookup(phone)
        print_gradient("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
