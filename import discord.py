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

intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)


 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('https://www.youtube.com/'):
        print (message.content)
        channelURL = message.content
        await message.delete()


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
                    channel_id_link = "https://youtube.com/channel/"+channel_id
                    
                    
                    # Prints Channel information to console #
                    print("Channel ID: "+channel_id)
                    print("Channel Name: "+channel_name)
                    print("Channel Logo: "+channel_logo)
                    print("Channel ID: "+channel_id_link)
                    
                    # Creates HTML file var# 
                    f = open('channelid.html','w')
                    
                
                    # Converts and downlaods image file to png # 
                    imgUrl = channel_logo
                    filename = "image.png".split('/')[-1]
                    r = requests.get(imgUrl, allow_redirects=True)
                    open(filename, 'wb').write(r.content)
                    
                    await message.channel.send(channel_id_link)

client.run("token")