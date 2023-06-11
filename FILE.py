import os, platform, time, sys

import requests

import time

import os

from sys import stderr



def jala(z):

	for e in z + '\n':

		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)

try:

	import requests

except ImportError:

	jala('\033[1;91m[\033[1;97m+\033[1;91m] \033[1;96minstall requests')

	os.system("pip install requests")



logo = ("""
  \033[1;91m   _____ __  _____    ____  __  _______   __
  \033[1;91m  / ___// / / /   |  / __ \/ / / /  _/ | / /
  \033[38;5;208m  \__ \/ /_/ / /| | / / / / /_/ // //  |/ / 
  \033[38;5;208m ___/ / __  / ___ |/ /_/ / __  // // /|  /  
  \033[1;95m/____/_/ /_/_/  |_/_____/_/ /_/___/_/ |_/ 
\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

LOGOS = ("""\033[1;92m
\033[1;97m ___  \033[1;92m_         \033[1;97m  ___  
\033[1;97m|  _|\033[1;92m\ \       \033[1;97m  |_  | 
\033[1;97m| |   \033[1;92m\ \         \033[1;97m | | 
\033[1;97m| |    \033[1;92m> >         \033[1;97m| | 
\033[1;97m| |_  \033[1;92m/ /\033[1;91m_______ \033[1;97m _| | 
\033[1;97m|___|\033[1;92m/_/\033[1;91m|_______|\033[1;97m|___| 
""")
LOGS = ("""\033[1;92m
                 ╔╗╴╴╴╔══════╗
                 ║║╴╴╴║╴╔════╝
                 ║╚═══╝╴╚════╗
                 ╚════╗╴╔═══╗║
                 ╔════╝╴║╴╴╴║║
                 ╚══════╝╴╴╴╚╝
""")


def menu():
	cookie_file_ = "fv_.txt"
	if os.path.isfile(cookie_file_):
		show_menu()
	else:
		with open("fv_.txt", "w") as file:
			file.write("")
			start_system()


import requests

def cookie(access_token):
    try:
        response = requests.get(f"https://www.facebook.com/?access_token={access_token}")
        cookies = response.cookies.get_dict()
        if 'c_user' in cookies and 'xs' in cookies:
            cookie = f"c_user={cookies['c_user']}; xs={cookies['xs']}"
            return cookie
        else:
            print("Failed to convert token to cookie. Please check your access token.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Read access token from file
filename = "Hannan_KinG007"  # Update with your file name
with open(filename, "r") as file:
    access_token = file.read().strip()

# Convert token to cookie
cookie_value = cookie(access_token)
if cookie_value:
    jalan(cookie_value)
    jala("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    input("\033[1;37m[\033[1;32m>\033[1;31m_\033[1;37m] \033[1;93mENTER TO MENU ")
    show_menu()
else:
    jala("\033[1;32mfast login new Facebook ID. uid and password")
    print("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(3)
    start_system()
    
    





def token():
    if os.path.exists("Hannan_KinG007"):
        with open("Hannan_KinG007", "r") as file:
            saved_pas = file.read().strip()
            jalan(saved_pas)
            jala("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            input("\033[1;37m[\033[1;32m>\033[1;31m_\033[1;37m] \033[1;93mENTER TO MENU ")
            show_menu()
    
        
     	

def watch_video():

    os.system("xdg-open https://fb.watch/kC4uRFCBog/?mibextid=NnVzG8")

    time.sleep(2.4)

    show_menu()


import requests




def show_menu():
	cookie_file_path = "Hannan_KinG07"
	if os.path.isfile(cookie_file_path):
		status = "\033[1;36mACTIVE\033[1;37m]"
	else:
		status = "\033[1;31mNONE\033[1;37m]  "
	os.system("clear")
	print('\x1b[1;97m[\x1b[1;92m' + status + '\x1b[1;95m                      \x1b[1;97m[\x1b[1;92mcookie\x1b[1;97m]\x1b[1;96m/\x1b[1;97m[\x1b[1;93mtoken\x1b[1;97m]')

	print(logo)

	print("\033[1;37m [1] \033[1;32m FB id dump menu \033[1;37m [\033[1;33m>_\033[1;37m]  \033[1;36m   ______  __ ")
	print("\033[1;37m [2] \033[1;32m show FB cookie  \033[1;37m [\033[1;33m>_\033[1;37m]   \033[1;36m |_  /\ \/ /")
	print("\033[1;37m [3] \033[1;32m show FB token   \033[1;37m [\033[1;33m>_\033[1;37m]    \033[1;36m / /  >  < ")
	print("\033[1;37m [4] \033[1;33m Watch dump video \033[1;37m[\033[1;33m>_\033[1;37m]   \033[1;36m /___|/_/\_\ ")
	print("\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

	umit =input("\033[1;37m [?] Choose :\033[1;32m ")

	if umit in ["1", "01"]:

		start_system()

	if umit in ["2","02"]:
		os.system("clear")
		print(LOGOS)
		jala("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;32m")

		cookie()
	if umit in ["3","03"]:
		os.system("clear")
		print(LOGOS)

		jala("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;33m")

		token()
	if umit in ["4", "04"]:
		watch_video()
	if umit in ["5", "05"]:
		exit("Exiting the system. Goodbye!")
	else:
		show_menu()


def start_system():
    os.system("clear")
    print(LOGS)
    jala("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;33m")
    print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mChecking For Update...')
    os.system('git pull --quiet 2>/dev/null')

    bit = platform.architecture()[0]

    if bit == '64bit':

    	print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m64Bit Found')

    	import FILE64

    elif bit == '32bit':

    	print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m32Bit Found')

    	import FILE32

    	

menu()

    
