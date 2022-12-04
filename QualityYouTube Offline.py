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

def exel(channel_name, channel_id_link, channel_id):
    


    # Give the location of the file
    path = "C:\\Users\\tom87\\test\\channels.xlsx"

    workbook_obj = openpyxl.load_workbook(path)
    sheet_obj = workbook_obj.active
    col2 = channel_name
    col3 = channel_id_link
    col4 = channel_id
    col1 = "None"
    sheet_obj.append([col1, col2, col3, col4])
    workbook_obj.save(path)

def exel2(channel_name, channel_id_link, channel_id, channel_logo):
    


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

def url():
    print("Plese enter a channel or video url..")

    channelURL = input()
    x = channelURL
    
    return channelURL

channelURL = url()
    
       
YouTubeDomain = "https://www.youtube.com/channel/"      
    
def error(channelURL):
    if re.search("http", channelURL):
        if re.search("://", channelURL):
            
            print("The url you supported has not been accepted. ")
        else:
            print("Not a URL.")
    else:
        print("Not a URL.")
    

## Processing URL ##


if re.search("http", channelURL):
    if re.search("://", channelURL):
        if re.search("youtu",channelURL):
            if re.search("/user/", channelURL):
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
    
    
                exel(channel_name, channel_id_link, channel_id, channel_logo)
            elif re.search("/c/", channelURL):
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
    
                
                
                
                
    
                exel(channel_name, channel_id_link, channel_id, channel_logo)
                print("/c/")
            elif re.search("/channel/", channelURL):
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
    
                
                
                
                
    
                exel(channel_name, channel_id_link, channel_id, channel_logo)
                print("/channel/")
            elif re.search("/@", channelURL):
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
    
                exel(channel_name, channel_id_link, channel_id, channel_logo)
            elif re.search("youtu.be", channelURL):
                YTV = YouTube(channelURL)
                channel_id = YTV.channel_id
                channel_id_link = YTV.channel_url

                c = Channel(channel_id_link)
                channel_name =c.channel_name
                
                
                
                print("Channel ID: "+channel_id)
                print("Channel Name: "+channel_name)
                print("Channel ID: "+channel_id_link)
    
                exel2(channel_name, channel_id_link, channel_id)
                print("Extracted from video link.")
            elif re.search ("com/watch", channelURL):
                YTV = YouTube(channelURL)
                channel_id = YTV.channel_id
                channel_id_link = YTV.channel_url

                c = Channel(channel_id_link)
                channel_name =c.channel_name
                
                
                
                soup = BeautifulSoup(requests.get(channel_id_link, cookies={'CONSENT': 'YES+1'}).text, "html.parser")
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
                
                
                
                
    
                exel2(channel_name, channel_id_link, channel_id)
                print("Extracted from video link.")
            elif re.search ("/shorts/", channelURL): 
                YTV = YouTube(channelURL)
                channel_id = YTV.channel_id
                channel_id_link = YTV.channel_url

                c = Channel(channel_id_link)
                channel_name =c.channel_name
                
                
                
                soup = BeautifulSoup(requests.get(channel_id_link, cookies={'CONSENT': 'YES+1'}).text, "html.parser")
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
                
                
                
                
                
                exel2(channel_name, channel_id_link, channel_id)
                print("Extracted from Shorts link.")
            else:
                
                error = error(channelURL)
                error()
                

    
    