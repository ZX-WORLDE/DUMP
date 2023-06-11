
import os

import requests

def jala(z):

	for e in z + '\n':

		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def get_facebook_cookie(access_token):
    # Create a session
    session = requests.session()

    # Make a request to log in and obtain the cookie
    log_data = {'access_token': access_token}
    header_freefb = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=log_data, headers=header_freefb)

    # Extract the cookie from the session
    log_cookies = session.cookies.get_dict().keys()
    if 'c_user' in log_cookies:
        cookie = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
        cid = cookie[7:22]
        return cookie

    return None

filename = "Hannan_KinG007"
if os.path.exists(filename):
    with open(filename, "r") as file:
        access_token = file.read().strip()
        
        cookie = get_facebook_cookie(access_token)
        if cookie:
            jalan(cookie)
            jala("\033[1;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            input("\033[1;37m[\033[1;32m>\033[1;31m_\033[1;37m] \033[1;93mENTER TO MENU ")
            os.system("python FILE.py")
        else:
            print("Failed to obtain the Facebook cookie.")
else:
    print("Access token file not found.")
