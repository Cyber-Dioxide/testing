import time
from colorama import Fore
from os import system
from sys import argv
import random

import pyfiglet

system("clear")
logo = pyfiglet.figlet_format("Caller")

W = Fore.LIGHTWHITE_EX
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
C = Fore.CYAN



for i in logo:
    ran = random.choice([W, G, Y, R, C])
    print(ran + i , end="")


NUM = argv[1]

print("\n\n")

print(W + "\t  ~Ongoing Call:~ " + C + NUM)

print("\n")

def main():
    min = 0
    hrs = 0
    sec = 0

    while True:
        if sec == 59:
            min += 1
            sec = 0

        if min == 59:
            hrs += 1
            min = 0

        if hrs == 24:
            hrs = 0

        print(f"{W}~: {C} Time elapsed: {W}{hrs}:{Y}{min}:{G}{sec} {W}:~" , end='\r')

        sec += 1

        time.sleep(0.1)

main()