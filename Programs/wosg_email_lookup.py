import re
import os
from colorama import init
from modules import email_harvester

init(autoreset=True)

# Yellow -> Dark Red gradient
GRADIENT = [
    "\033[38;2;255;255;0m",   # Yellow
    "\033[38;2;255;200;0m",
    "\033[38;2;255;165;0m",
    "\033[38;2;255;120;0m",
    "\033[38;2;220;60;0m",
    "\033[38;2;139;0;0m",     # Dark Red
    "\033[0m"
]

def gradient_text(text):
    result = ""
    length = len(text)
    steps = len(GRADIENT) - 1
    for i, c in enumerate(text):
        color_index = int(i / max(length, 1) * steps)
        result += GRADIENT[color_index] + c
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

                  WINDOWS ONLY FOR RN     
             https://discord.gg/m4Jc2Mj9Fy
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    clear()
    print(gradient_text(BANNER))

    domain = input(gradient_text("\n[+] Enter domain: "))
    pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"

    if not re.match(pattern, domain):
        print(gradient_text("\n[-] Invalid domain"))
        return

    print(gradient_text(f"\n[+] Starting email harvest on: {domain}\n"))
    email_harvester.target(domain)

if __name__ == "__main__":
    main()
