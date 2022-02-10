import sys,os
try:
    from colorama import Fore

except ModuleNotFoundError:
    os.system("pip install colorama")


from platform import platform
def cmd(str):
    os.system(str)

# cmd("apt install ruby")

os.system("cls") if "Windows" in platform() else os.system("clear")

R = Fore.RED
W = Fore.LIGHTWHITE_EX
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW


if sys.argv[0].isalpha():
    print(W +"Usage: python3 run.py [range of ip]")
    print(C +"Note: range of ip should be numeric.")
    exit()

if sys.argv[0] == "":
    print(R +"Usage: python3 run.py [range of ip]")
    print(G +"Note: range of ip should be numeric.")
    exit()

if sys.argv[0].isalnum():
    print(R + "Usage: python3 run.py [range of ip]")
    print(G + "Note: range of ip should be numeric.")
    exit()


if sys.argv[0].isdigit():
    rang = sys.argv[0]

    cmd(f"ruby Gen.rb {rang}")


