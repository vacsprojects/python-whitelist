# Whitelist wont really be a "whitelist" if you dont obfuscate it. I recommend pyarmor.

import requests 
import time
import os

os.system("cls")

ipdb = requests.get("https://pastebin.com/raw/9eeV4yWA").text # ipdb = ["MYIP, MYIP1, MYIP2"]
                                                                #Format ^^^^^^^^^^^^^^^^^^^^^
# Database is deleted from github so you cannot view.


ip = requests.get("https://api.ipify.org").text # ip = YOURIP
                                                #format ^^
i = 1 #placeholder

while i < 10:
    os.system("cls")
    print("Checking database...")
    time.sleep(0.5)
    if ip in ipdb: # Checks if your ip is in database.
        os.system("cls")
        i = 11
        print("Sucessfully logged in.")
        input() # So program doesnt close, allows user to read output if they open directly from file explorer.
    else: #Anything Else
        i = 11
        os.system("cls")
        print("IP not found in our database.")
        time.sleep(1)
        print("Exiting Program...")
        time.sleep(0.7)
        exit()
