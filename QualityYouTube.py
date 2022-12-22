import re
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
from configparser import ConfigParser
import discord
from pytube import YouTube
from pytube import Channel
from discord.ext import commands
import mysql.connector


intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
YouTubeDomain = "https://www.youtube.com/channel/"

# Creates or checks for config
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f) 
else:
    print("Please enter your token and the channel ID of the Discord channel you'd like to use.")
    print("If left blank, you'll need to go to the config.json to set them.")
    token = str(input("Bot Token: ") or "token goes here...")
    discordChannel = str(input("Channel ID:  ") or "000000000000000000")
    configTemplate = {"Token": (token), "Prefix": "!","discordChannel": (discordChannel)}
    print("The script will now crash and show an error. Run 'python QualityYouTube.py' again.")
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 
token = configData["Token"]
prefix = configData["Prefix"]
discordChannel = configData["discordChannel"]
# Boots up the bot 
@client.event

async def on_ready():
    client.run
    discordChannelInt = int(discordChannel)
    discordName = client.get_channel(discordChannelInt)
    print('We have logged in as {0.user}'.format(client))
    print('Using Discord channel: ', discordName)
    print('The bot has now fully booted up and may be used. \nPlease be advised this bot only supports one Discord server at a time. Future updates will allow for more than one server to be active at a time.')
    
    
# Bot is checking messages
@client.event
async def on_message(message):
    author = message.author
    timeOutMessage10 = " This message will be deleted in 10 seounds."
    timeOutMessage60 = " This message will be deleted in 60 seounds."
    noURL = " This does not contain a URL."
    invalidURL = " This URL is not supported. Please enter a valid URL."
    notChannel =  """Make sure the channel follows one of the following formats starting with http or https. 
    \r - http:://youtube.com/user/username
    \r - http://youtube.com/channel/username
    \r - http://youtube.com/@username\r\r
    ***We hope to add video support soon***"""
    timeStanpIncluded = "Please remove the time stamp from the URL.\nhttps://youtu.be/agEapr94odU?t=100 -> https://youtu.be/agEapr94odU\n Basically remove the ***?t=100***\n"
    youTubeViwers = 'You may also find sucess in repasting the channel inside chat, sometimes the bot bugs out and posts a channel called "YouTube Viwers" without reason'
    num60 = 60
    num10 = 10
    if message.author == client.user:
       return    
    
    
    discordChannelInt = int(discordChannel)
    if discordChannelInt == message.channel.id:
        channelURL = message.content
        if re.search("http", message.content):
            if re.search("http", channelURL) and search("://", channelURL) and search("youtu", channelURL):
                await message.delete()
                if re.search ("/channel/", channelURL) or re.search ("@", channelURL) or re.search ("/user/", channelURL) or re.search ("/c/", channelURL):
                    soup = BeautifulSoup(requests.get(channelURL, cookies={'CONSENT': 'YES+1'}).text, "html.parser")
                    data = re.search(r"var ytInitialData = ({.*});", str(soup.prettify())).group(1)
                    json_data = json.loads(data)
                
                    channel_id   = json_data["header"]["c4TabbedHeaderRenderer"]["channelId"]
                    channel_name = json_data["header"]["c4TabbedHeaderRenderer"]["title"]
                    channel_logo = json_data["header"]["c4TabbedHeaderRenderer"]["avatar"]["thumbnails"][2]["url"]
                    channel_id_link = YouTubeDomain+channel_id
                    print("Channel ID: "+channel_id)
                    print("Channel Name: "+channel_name)
                    print("Channel Logo: "+channel_logo)
                    print("Channel ID: "+channel_id_link)
                    
                elif re.search ("com/watch", channelURL) or re.search ("/shorts/", channelURL) or re.search ("youtu.be", channelURL) or re.search("?list=", channelURL):
                    YTV = YouTube(channelURL)
                    channel_id = YTV.channel_id
                    channel_id_link = YTV.channel_url

                    c = Channel(channel_id_link)
                    channel_name =c.channel_name
                    
                    
                    
                    print("Channel ID: "+channel_id)
                    print("Channel Name: "+channel_name)
                    print("Channel ID: "+channel_id_link)
        
        
                            
            
            if re.search ("UCMDQxm7cUx3yXkfeHa5zJIQ", channel_id_link):
                await message.channel.send(timeStanpIncluded+timeOutMessage10+"\n\n\n"+youTubeViwers, delete_after=num10)
            else:
                await message.channel.send(channel_name+" - "+channel_id_link)     
            
        else:
    
            print("""Link not supported or wrong channel.
Link was posted insice channel """+message.channel.name)
    else:
        return                   

    

client.run(token)