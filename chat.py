import os
import requests
import pyscreenshot as ImageGrab

import datetime as dt

def message(title, message):
    """ubuntu рүү notif явуулах нь"""
    os.system('notify-send "'+title+'" "'+message+'"')

tsag_burtgel_channel_id = ""
test_channel_id = ""

discord_url = f"https://discord.com/api/v9/channels/{tsag_burtgel_channel_id}/messages"

headers = {
    "authorization": ""
}

payload = {
    "content": "",
}

first = 1920 + (1920 / 3)
dooshoo_undur = 100
urt = first + 600
deerees_zai = 0

# grab fullscreen
im = ImageGrab.grab(bbox=(first, deerees_zai, urt, dooshoo_undur))

today = str(dt.datetime.today())
file_name = f"{today}.png"

# save image file
im.save(file_name)

# File
files = {
    "file" : (file_name, open(file_name, 'rb')) # The picture that we want to send in binary
}

r = requests.post(discord_url, data=payload, headers=headers, files=files)
os.remove(file_name)
if r.ok:
    message(str(today), "Зураг явуулсан")
else:
    message(str(today), "Зураг явуулахад алдаа гарсан байна")
