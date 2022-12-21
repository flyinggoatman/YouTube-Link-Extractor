import base64
import json
import os
import re
import time
import webbrowser
from configparser import ConfigParser
from re import search
from urllib.request import urlopen
from PIL import Image
import discord
import pyautogui
import pyperclip
import requests
from bs4 import BeautifulSoup
from pytube import Channel, YouTube
from imgurpython import ImgurClient
from datetime import datetime
import shutil

intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
YouTubeDomain = "https://www.youtube.com/channel/"

def LogoUpload(channel_name, filename, channel_id_link):
    imagePath = filename
    albumID = "Quality YouTube Channel Logos"
    '''
		Upload a picture of a kitten. We don't ship one, so get creative!
	'''

	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
    config = {
            'album': albumID,
            'name':  channel_name,
            'title': channel_name,
            'description': channel_id_link+' '.format(datetime.now())
    }
    print(ImgurClient)
    print("Uploading image... ")
    image = client.upload_from_path(filename, config=config, anon=False)
    print("Uploaded")
    print()


# If you want to run this as a standalone script


# Creates or checks for config
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f) 
        
else:
    print("Please enter your token and the channel ID of the Discord channel you'd like to use.")
    print("If left blank, you'll need to go to the config.json to set them.")
    token = str(input("Bot Token: ") or "token goes here...")
    discordChannel = str(input("Channel ID:  ") or "000000000000000000")
    configTemplate = {"Token": (token), "Prefix": "!","discordChannel": (discordChannel),"SQLHost":"HOST", "SQLUser": "USER","SQLPass": "PASS", "SQLDatabase": "DATABASE"}
    print("The script will now crash and show an error. Run 'python QualityYouTube.py' again.")
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f) 
token = configData["Token"]
prefix = configData["Prefix"]
discordChannel = configData["discordChannel"]
#beta features
sqlhost = configData["SQLHost"]
sqluser = configData["SQLUser"]
sqlpass = configData["SQLPass"]
sqldata = configData["SQLDatabase"]
print(sqlhost+"\n"+sqluser+"\n"+sqlpass+"\n"+sqldata)




if os.path.exists(os.getcwd() + "/configImgur.json"):
    with open("./configImgur.json") as f:
        configDataImgur = json.load(f) 
        print('Generating Imgur config file. Please see"configImgur.json" to change credentials')
else:
        #imgur config
    configTemplateImgur = {"ImgurToken": "" , "ClientID": "","ClientSecret": "","Username": ""}
    with open(os.getcwd() + "/configImgur.json", "w+") as f:
        json.dump(configTemplateImgur, f) 
ImgurToken = configDataImgur["ImgurToken"]
ImgurID = configDataImgur["ClientID"]
ImgurSecret = configDataImgur["ClientSecret"]
ImgurUsername = configDataImgur["Username"]
    
ImgurClient = ImgurClient(ImgurID, ImgurSecret, ImgurToken)
print("Complete")
imgur_token = ImgurToken

# Boots up the bot 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
# Bot is checking messages
@client.event
async def on_message(message):
    author = message.author
    timeOutMessage10 = " This message will be deleted in 10 seconds."
    timeOutMessage60 = " This message will be deleted in 60 seconds."
    noURL = " This does not contain a URL."
    invalidURL = " This URL is not supported. Please enter a valid URL."
    notChannel =  """Make sure the channel follows one of the following formats starting with http or https. 
    \r - http:://youtube.com/user/username
    \r - http://youtube.com/channel/username
    \r - http://youtube.com/@username\r\r
    ***We hope to add video support soon***"""
    timeStampIncluded = "Please remove the time stamp from the URL.\nhttps://youtu.be/agEapr94odU?t=100 -> https://youtu.be/agEapr94odU\n Basically remove the ***?t=100***\n"
    youTubeViwers = 'You may also find sucess in repasting the channel inside chat, sometimes the bot bugs out and posts a channel called "YouTube Viwers" without reason'
    num60 = 60
    num10 = 10
    if message.author == client.user:
       return    
    if re.search("http", message.content):
        channelURL = message.content
        discordChannelInt = int(discordChannel)
        if (discordChannelInt == message.channel.id):
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
                    print("Channel Link: "+channel_id_link)
                    
                    
                    
                    imgUrl = channel_logo
                    filename = channel_name+".png".split('/')[-1]
                    r = requests.get(imgUrl, allow_redirects=True)
                    open(filename, 'wb').write(r.content)
                    LogoUpload(filename, channel_name, channel_id_link)
                    
                elif re.search ("com/watch", channelURL) or re.search ("/shorts/", channelURL) or re.search ("youtu.be", channelURL):
                    YTV = YouTube(channelURL)
                    channel_id = YTV.channel_id
                    channel_id_link = YTV.channel_url

                    c = Channel(channel_id_link)
                    channel_name =c.channel_name
                    
                    
                    
                    print("Channel ID: "+channel_id)
                    print("Channel Name: "+channel_name)
                    print("Channel ID: "+channel_id_link)
        
        
                            
            
            if re.search ("UCMDQxm7cUx3yXkfeHa5zJIQ", channel_id_link):
                await message.channel.send(timeStampIncluded+timeOutMessage10+"\n\n\n"+youTubeViwers, delete_after=num10)
            else:
                await message.channel.send(channel_name+" - "+channel_id_link)
                
            
        elif message.content.endswith('.com/'):
            await message.channel.send(author.mention+notChannel+timeOutMessage60, delete_after=num60)
        elif not message.content.includes('channel') or message.content('user') or message.content('@'):
            author = message.author
            await message.channel.send(author.mention+invalidURL+timeOutMessage60, delete_after=num60)
        elif message.content.excludes('.com') or message.content.excludes('www') or message.content.excludes(''):
            author = message.author
            await message.channel.send(author.mention+noURL+timeOutMessage10, delete_after=num10)
        else:
                
                print("incorrect channel")
                        

    

client.run(token)