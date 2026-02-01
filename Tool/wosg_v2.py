from colorama import Fore, Style

import os

banner = f"""{Fore.RED}
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

menu = f"""{Fore.RED}
+---OSINT THINGS---+=========+---OTHER THINGS---+
+  [1] Phone       +=========+  [4] Dc Osint    +
+  [2] IP          +=========+  [5] Credits     +
+  [3] E-Mail      +=========+  [6] Exit        +
+------------------+=========+------------------+
"""

dox_tuto = f"""{Fore.RED}
Social Engineering: Social engineering is a technique used to manipulate people into doing something they wouldn't normally do. It involves tricking them into revealing sensitive information or gaining access to their systems. This can be done through various methods such as phishing, pretexting, baiting, and pretexting. For example, you could create a fake profile on a social media platform and befriend someone, then trick them into revealing their street, full name or such. You can also use social engineering to trick them into installing malware on their device, which can be used to steal their IP address and way more.

Tools: There are several tools available for resolving Discord IDs to IP addresses. For example OGsint, and sometimes even Discord ID Lookups. These tools can be found on various websites and forums. You can also use online services like IP Logger to log IP addresses from Discord messages. And there is also a tool online that can get a person's warnings on Discord by their ID, which can also reveal good material.

Databases: There are several databases available that contain IP addresses and Discord IDs. You can find these databases on various websites and forums. You can also use your own database if you have collected the information through other means. The best databases are by RestoreCord, where if you dm FestivePup in the server you will get an 860k user one for free (More for money). Be careful when using these databases, as they may be outdated or contain incorrect information.

"""

tool_creds = f"""
Tool Creator: @rp9y

Discord Server Link: https://discord.gg/m4Jc2Mj9Fy

-------------
----THANK----
-----YOU-----
-------------
"""

def main_func():
    print(banner, menu)
    maininput = input("[wosg@MAIN] > ")

    if maininput == '1':
        os.system("python wosg_phone_lookup.py")
    elif maininput == '2':
        os.system("python wosg_ip_lookup.py")
    elif maininput == '3':
        os.system("python wosg_email_lookup.py")
    elif maininput == '4':
        print(dox_tuto)
    elif maininput == '5':
        print(tool_creds)
    elif maininput == '6':
        exit

main_func()
