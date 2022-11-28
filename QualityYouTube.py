import discord
import re
import easygui
from easygui import *
from re import search
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import json
import base64
import os
import webbrowser
import pyperclip
import win32com.client as comclt
import time
import pyautogui
import discord
from configparser import ConfigParser
import datetime
import datetime


now = datetime.datetime.now()






intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)


# Creates or checks for config
if os.path.exists(os.getcwd() + "/config.json"):
    
    with open ("./config.json") as f:
        configData = json.load(f)
            
else:
    easygui.textbox("Whats your token?")
    token =  easygui.textbox()
    configTemplate = {"token": token, "Prefix": "!", "DiscordChannel": "DiscordChannel"}
    
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["token"]
prefix = configData["Prefix"]
discordChannel = configData["DiscordChannel"]

 
 
# Boots up the bot 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
# Bot is checking messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('/channel '):
        print (message.content)
        channelURL = message.content
        channelURL = channelURL.replace("/channel ", "")
        await message.delete()
    if message.channel.id == 938207947878703187:
        # await message.channel.send("")
        if search("http", channelURL):
                if re.search("://", channelURL):
                    if re.search("youtu", channelURL):
                        
                        # Loads page data #
                        soup = BeautifulSoup(requests.get(channelURL, cookies={'CONSENT': 'YES+1'}).text, "html.parser")
                        data = re.search(r"var ytInitialData = ({.*});", str(soup.prettify())).group(1)
                        json_data = json.loads(data)
                        
                        # Finds channel information #
                        channel_id   = json_data["header"]["c4TabbedHeaderRenderer"]["channelId"]
                        channel_name = json_data["header"]["c4TabbedHeaderRenderer"]["title"]
                        channel_logo = json_data["header"]["c4TabbedHeaderRenderer"]["avatar"]["thumbnails"][2]["url"]
                        channel_id_link = "https://www.youtube.com/channel/"+channel_id
                        
                        
                        # Prints Channel information to console #
                        print("Channel ID: "+channel_id)
                        print("Channel Name: "+channel_name)
                        print("Channel Logo: "+channel_logo)
                        print("Channel ID: "+channel_id_link)
                        
                        
                    
                        # Converts and downlaods image file to png # 
                        imgUrl = channel_logo
                        filename = "image.png".split('/')[-1]
                        r = requests.get(imgUrl, allow_redirects=True)
                        open(filename, 'wb').write(r.content)
                        
                        author = message.author
                       
                        #Messages
                        Message_1 = channel_name+" was posted by "+(author.mention)+"(now.shifttime(""))"+""
                        timeOutMessage10 = " This message will be deleted in 10 seounds."
                        timeOutMessage60 = " This message will be deleted in 60 seounds."
                        noURL = " This does not contain a URL."
                        invalidURL = " This URL is not supported. Please enter a valid URL."
                        notChannel =  """Make sure the channel follows one of the following formats starting with http or https. 
                        \r - http:://youtube.com/user/username
                        \r - http://youtube.com/channel/username
                        \r - http://youtube.com/@username\r\r
                        ***We hope to add video support soon***"""
                        num60 = 60
                        num10 = 10
                        
                        
                        
                        await message.channel.send(channel_id_link)
                    elif message.content.endswith('.com/'):
                        await message.channel.send(author.mention+notChannel+timeOutMessage60, delete_after=num60)
                    elif not message.content.includes('channel') or message.content('user') or message.content('@'):
                        author = message.author
                        await message.channel.send(author.mention+invalidURL+timeOutMessage10, delete_after=num60)
        elif message.content.excludes('.com') or message.content.excludes('wwww') or message.content.excludes(''):
                        author = message.author
                        await message.channel.send(author.mention+noURL+timeOutMessage10, delete_after=num10)
    else: 
        print("Wrong Channel")
        

client.run(token)