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



channel = easygui.enterbox("Enter channel or video link?")

if search("http", channel):
    if re.search("://", channel):
        if re.search("youtu", channel):
            
            # Loads page data #
            soup = BeautifulSoup(requests.get(channel, cookies={'CONSENT': 'YES+1'}).text, "html.parser")
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
            
            
            
            # Creates HTML file #
            message = """<html>
            <head></head>c
            <body>
            <p>
            <center>
            <br>"""+channel_name+"""</br>
            <br><a href="""+channel_id_link+""")>"""+channel_id_link+"""</a></br>
            <br><img src="image.png"></br>
            </center>
            </body>
            </html>"""

            f.write(message)
            f.close()
            # Opens HTNL file in new browser. #
            webbrowser.open_new('channelid.html')
            
            # Copies channel ID url to clipboard. #
            pyperclip.copy(channel_id_link)
            
            #Opens discord #
            discord = '#discord channel link#'
            webbrowser.open_new_tab(discord)
            time.sleep(8)
            with pyautogui.hotkey('ctrl', 'v'):
                 pyautogui.press('Enter')
            
            
            
            # pyautogui.hold('ctrl'):
            #     pyautogui.press(['v'])
            #         pyautogui.hotkey()
#             The effect is that calling hotkey('ctrl', 'shift', 'c') would perform a "Ctrl-Shift-C" hotkey/keyboard shortcut press.
# else:
    easygui.msgbox("Llnk not supported.")
    
                        
                        
                        # https://www.youtube.com/@elespiritudelvolcan/channels
                            # page = urlopen(channel)
                            # soup = BeautifulSoup(page, 'html.parser')
                            # content = soup.find("span", itemprop="url")
                            # print(content)
                        # output = easygui.ynbox("Shall I continue?", 'Title', ("Yes", "No"))