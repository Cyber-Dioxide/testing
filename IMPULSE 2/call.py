import os
import sys

from colorama import Fore

try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")

import random
from time import sleep


name = pyfiglet.figlet_format("CALLER")

W = Fore.LIGHTWHITE_EX
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN



def slow(str):
    for i in str + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(5/90)

def main():
    os.system("clear")
    for i in name:
        ran = random.choice([W, G, R, Y, C])
        print(ran+i , end="")

    print("\n")
    print(f"{W}Your number: {Y}{sys.argv[1]}")
    num = input(W + "Number:~ " + Y)
    token = str(random.randint(10000 , 99999)) + "-" + str(random.randint(10000 , 9999))
    print(W+  f"\n{Y}~ {C}Generating Authtoken please wait... {Y}~")
    sleep(3)
    print(f"{C}</> Your Authtoken: ~ {W}{token}")

    print(W + pyfiglet.figlet_format("Dialer"))
    print("\n\n")
    slow(W + "Number :" +C + num)
    os.system(f"python3 time.py {num}")

main()

