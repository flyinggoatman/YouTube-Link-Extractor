import re
from re import search
from urllib.request import urlopen
import requests
import re
import base64
import os
import pyperclip
import win32com.client as comclt
import time
import pyautogui
from configparser import ConfigParser
from pytube import YouTube
from pytube import Channel
from bs4 import BeautifulSoup
import json
import openpyxl

## This is meant to create a exel file containing all the channels that have been procesed.

YouTubeDomain = "https://www.youtube.com/channel/"
def exel(channel_name, channel_id_link, channel_id, channel_logo):
    


    # Give the location of the file
    path = "C:\\Users\\tom87\\test\\channels.xlsx"

    workbook_obj = openpyxl.load_workbook(path)
    sheet_obj = workbook_obj.active
    col2 = channel_name
    col3 = channel_id_link
    col4 = channel_id
    col1 = channel_logo
    sheet_obj.append([col1, col2, col3, col4])
    sheet_obj.append([col1])
    workbook_obj.save(path)



## This function takes video links and converts them into channelURLs to be processed by the beautifulSoup function.    
def videoVersion(channelURL):
    YTV = YouTube(channelURL)
    channelURL = YTV.channel_url
    print(videoVersion)
    return channelURL
    

    
# I can't remember why I have two of these.
def videoVersion():
    YTV = YouTube(channelURL)
    channel_id = YTV.channel_id
    channel_id_link = YTV.channel_url

    c = Channel(channel_id_link)
    channel_name =c.channel_name
    return channel_id_link, channelURL
    
# This takes a channel URL and converts it to the desired infomation.    
def BeautifulSoup1(channelURL):
    soup = BeautifulSoup(requests.get(channelURL, cookies={'CONSENT': 'YES+1'}).text, "html.parser")
    data = re.search(r"var ytInitialData = ({.*});", str(soup.prettify())).group(1)
    json_data = json.loads(data)

    channel_id   = json_data["header"]["c4TabbedHeaderRenderer"]["channelId"]
    channel_name = json_data["header"]["c4TabbedHeaderRenderer"]["title"]
    channel_logo = json_data["header"]["c4TabbedHeaderRenderer"]["avatar"]["thumbnails"][2]["url"]
    channel_id_link = YouTubeDomain+channel_id
    
    # The following code is checking to see if the channel is a channel that is a bug in the code.
    # Sometimes "YouTube Viewers" is found instead of the owner of the video or channel.
    # This mostly happens when the URL contains a timestamp I think.
    if re.search("YouTube Viewers", channel_name):
        print("error")
        BeautifulSoup1(channelURL)
    else:
        # This prints the channels information
        print("Channel ID: "+channel_id)
        print("Channel Name: "+channel_name)
        print("Channel Logo: "+channel_logo)
        print("Channel ID: "+channel_id_link)
        return channel_name, channel_id_link, channel_id, channel_logo



     
    
def error(channelURL):
    if re.search("http", channelURL):
        if re.search("://", channelURL):
            
            print("The url you supported has not been accepted. ")
        else:
            print("Not a URL.")
    else:
        print("Not a URL.")
    

## Processing URL ##

# The following variable is a test one. You can change it to a channel or video url.
channelURL = "https://www.youtube.com/watch?v=CpIAmXmM4uc"


#This takes the channelURL and decides if it's a video or channel URL and then if it's one of the supported urls.
if re.search("http", channelURL) and re.search("://", channelURL) and re.search("youtu",channelURL):

    if re.search("/user/", channelURL) or re.search("/c/", channelURL) or re.search("/channel/", channelURL) or re.search("/@", channelURL):
        
        channel_name, channel_id_link, channel_id, channel_logo = BeautifulSoup1(channelURL)

        exel(channel_name, channel_id_link, channel_id, channel_logo)
        print("/channel/")
    elif re.search("youtu.be", channelURL) or re.search("com/watch", channelURL) or re.search("/shorts/", channelURL):
        
        
        channel_id_link, video = videoVersion()
        channelURL = channel_id_link
        channel_name, channel_id_link, channel_id, channel_logo = BeautifulSoup1(channelURL)

        exel(channel_name, channel_id_link, channel_id, channel_logo)
        print("Extracted from video link.")
    else:
        
        print("Error")
                

    
    