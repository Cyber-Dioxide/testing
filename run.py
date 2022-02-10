import sys,os
try:
    from colorama import Fore

except ModuleNotFoundError:
    os.system("pip install colorama")


from platform import platform
def cmd(str):
    os.system(str)



os.system("cls") if "Windows" in platform() else os.system("clear")

R = Fore.RED
W = Fore.LIGHTWHITE_EX
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW

print(sys.argv[1])

rang = sys.argv[1]



cmd("apt install ruby")

cmd(f"ruby Gen.rb {rang}")


