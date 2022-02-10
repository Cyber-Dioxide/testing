import sys,os , string
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


for i in string.ascii_letters:
    for j in sys.argv[1]:
        if i == j:

            print(R + "[@] Usage: python3 run.py [range of ip's]")
            print(G + "[>] Note: Range of ip's should be numeric")
            exit()

    

rang = sys.argv[1]



cmd("apt install ruby")

cmd(f"ruby Gen.rb {rang}")


