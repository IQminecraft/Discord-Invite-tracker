import requests
import json

def setup():
    link = input("Discordのinvite link : ")
    if "https://discord.gg/" in link:
        link = link.replace("https://discord.gg/", "")
        return link
    elif "discord.gg/" in link:
        link = link.replace("discord.gg/", "")
        return link
    else:
        print("正しいURLを入力してください")
        input()
        exit()

def send(link):
    r = requests.get(f"https://discord.com/api/v9/invites/{link}")
    return r.json()

def info(res):
    global inviter_id, inviter_name, guild_id, guild_name, guild_description, guild_icon, guild_banner, guild_splash, vanity_url_code
    inviter_name = res["inviter"]["username"]
    inviter_id = res["inviter"]["id"]
    guild_name = res["guild"]["name"]
    guild_id = res["guild"]["id"]
    guild_description = res["guild"]["description"]
    guild_icon = f'https://cdn.discordapp.com/icons/{res["guild"]["id"]}/{res["guild"]["icon"]}.webp?size=100'
    vanity_url_code = res["guild"]["vanity_url_code"]
    if not res["guild"]["banner"] == "None":
        guild_banner = f'https://cdn.discordapp.com/banners/{res["guild"]["id"]}/{res["guild"]["banner"]}.jpg?size=2048'
    if not res["guild"]["splash"] == "None":
        guild_splash = f'https://cdn.discordapp.com/splashes/{res["guild"]["id"]}/{res["guild"]["splash"]}.jpg?size=2048'


    

link = setup()
response = send(link)
info(response)
print(f"""

██╗███╗░░██╗██╗░░░██╗██╗████████╗███████╗██████╗░
██║████╗░██║██║░░░██║██║╚══██╔══╝██╔════╝██╔══██╗
██║██╔██╗██║╚██╗░██╔╝██║░░░██║░░░█████╗░░██████╔╝
██║██║╚████║░╚████╔╝░██║░░░██║░░░██╔══╝░░██╔══██╗
██║██║░╚███║░░╚██╔╝░░██║░░░██║░░░███████╗██║░░██║
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
Inviter name : {inviter_name}
Inviter ID : {inviter_id}

░██████╗░██╗░░░██╗██╗██╗░░░░░██████╗░
██╔════╝░██║░░░██║██║██║░░░░░██╔══██╗
██║░░██╗░██║░░░██║██║██║░░░░░██║░░██║
██║░░╚██╗██║░░░██║██║██║░░░░░██║░░██║
╚██████╔╝╚██████╔╝██║███████╗██████╔╝
░╚═════╝░░╚═════╝░╚═╝╚══════╝╚═════╝░
Guild Name : {guild_name}
Guild ID : {guild_id}
Guild Description : {guild_description}
Guild Icon : {guild_icon}
Guild Banner : {guild_banner if not guild_banner is None else "None"}
Guild Splash : {guild_splash if not guild_splash is None else "None"}
Default Link : {f"https://discord.gg/{vanity_url_code}" if not vanity_url_code is None else "None"}
""")
input()
