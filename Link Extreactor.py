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




channel = easygui.enterbox("Enter channel or video link?")

if search("http", channel):
    if re.search("://", channel):
        if re.search("youtu", channel):
            
            soup = BeautifulSoup(requests.get(channel, cookies={'CONSENT': 'YES+1'}).text, "html.parser")
            
            data = re.search(r"var ytInitialData = ({.*});", str(soup.prettify())).group(1)
            
            json_data = json.loads(data)
            
            channel_id   = json_data["header"]["c4TabbedHeaderRenderer"]["channelId"]
            channel_name = json_data["header"]["c4TabbedHeaderRenderer"]["title"]
            channel_logo = json_data["header"]["c4TabbedHeaderRenderer"]["avatar"]["thumbnails"][2]["url"]
            channel_id_link = "https://youtube.com/channel/"+channel_id
            
            print("Channel ID: "+channel_id)
            print("Channel Name: "+channel_name)
            print("Channel Logo: "+channel_logo)
            print("Channel ID: "+channel_id_link)
            

            f = open('channelid.html','w')
            
        

            imgUrl = channel_logo
            filename = "image.png".split('/')[-1]
            r = requests.get(imgUrl, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            
            
            

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

            webbrowser.open_new_tab('channelid.html')
            pyperclip.copy(channel_id_link)
else:
    easygui.msgbox("Llnk not supported.")
                        
                        
                        # https://www.youtube.com/@elespiritudelvolcan/channels
                            # page = urlopen(channel)
                            # soup = BeautifulSoup(page, 'html.parser')
                            # content = soup.find("span", itemprop="url")
                            # print(content)
                        # output = easygui.ynbox("Shall I continue?", 'Title', ("Yes", "No"))