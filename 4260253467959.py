
# @RASOUL_BOT
# @iD_RASOUL

#هر گونه ادیت یا ویرایش سورس حرام میباشد



auth = ["AUTH"]
#هرچقد اوت میخاید بزنید

link_post = "https://rubika.ir/rezaiat_RASOUL/EBJBIEJGJCAEIIJ"


time_forward = (0)

import os
from re import findall
from time import sleep
import time
import pyfiglet
import rainbowtext
from colorama import Fore
from random import choice
from datetime import datetime
from arsein import Messenger
os.system("clear")

magenta = "\033[95m"
cyan = "\033[95m"
bold = "\033[97m"
underline = "\033[4m"
red = "\033[31m" 
blue = "\033[36m" 
pink = "\033[35m" 
yellow = "\033[93m" 
darkblue = "\033[34m" 
white = "\033[00m"
green = "\033[32m" 

print (f"{yellow} @RASOUL_BOT\n\nلطفا صبور باشید . . .")

group = []


app = Messenger(choice(auth))

n = 0

message_id = app.Infolinkpost(link_post)["data"]["link"]["open_chat_data"]["message_id"]


object_guid = app.Infolinkpost(link_post)["data"]["link"]["open_chat_data"]["object_guid"]

linkdoni = ["c0BTXy05d5dbf4aa17e8c92e7e260973","c0Btyq095a83abe72ecf41080c6f1c35","c0Ee8O06d4d835c994ab8a51ea0e4880","c0Ee9X09008b057804dadf8f941e305a","c0RSKL05e95414cec64d48b54f2e943e","c0Btyq095a83abe72ecf41080c6f1c35","c0BLtCj0a67003dfd2457450497c5db8","c0Ee9X09008b057804dadf8f941e305a","c0Btyq095a83abe72ecf41080c6f1c35","c0MTeU0f77bd1c780b8b7509797bfd68"]



while True:
	for j in linkdoni:
		try:
			kk=app.joinChannelByGuid(j)
			last_message_id = app.getChannelInfo(j)["data"]["chat"]["last_message_id"]
			get_mesagges = app.getMessages(j, last_message_id)
			for text in get_mesagges:
				texts = text["text"]
				kl = findall(r"https://rubika.ir/joing/\w{32}", texts)
				for links in kl:
					group.append(links)
		except:
			pass
	for join in group:
		bot = Messenger(choice(auth))
		try:
			join_group = bot.joinGroup(join)
			name = join_group["data"]["group"]["group_title"]
			ghj = join_group["data"]["chat_update"]["chat"]["access"]
			if "SendMessages" in ghj:
				forr=bot.forwardMessages(object_guid, [message_id], join_group["data"]["group"]["group_guid"])
				count_seen =  forr['data']['message_updates'][0]['message']['count_seen']
				bot.leaveGroup(join_group["data"]["group"]["group_guid"])
				n+=1
				print (f"\n {green} ╭───── • ◆ • ─────╮\n"+f"\n{blue}   [=] - NAME group : "+f"{white}{name}\n" + f"{yellow}   [=] - GROUP status : " + f"{green}OPEN✓" + f"{blue}" + f"{pink}\n   [=] - TIME for : " + f"{white}" + datetime.now().strftime("%H:%M:%S") + "\n" + f"{darkblue}   [=] - NUMBER forward : " + f"{white}{n}" + f"\n{red}   [=] - SEEN post : "+ f"{white}{count_seen}" + f"\n\n {green} ╰───── • ◆ • ─────╯")
			else:
					print (f"\n {red} ╭───── • ◆ • ─────╮\n"+f"\n{blue}   [=] - NAME group : "+f"{white}{name}\n" + f"{yellow}   [=] - GROUP status : " + f"{red}CLOSED×" + f"{blue}" + f"{pink}\n   [=] - TIME for : " + f"{white}" + datetime.now().strftime("%H:%M:%S") + f"\n\n {red} ╰───── • ◆ • ─────╯")
					bot.leaveGroup(join_group["data"]["group"]["group_guid"])
					time.sleep(time_forward)
		except:
			pass