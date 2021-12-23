import random
import pyfiglet
import MyColors


lbiu = MyColors.lightColorsBIU()
nbiu = MyColors.NormalBIUColors()

nbold = MyColors.NormalBoldColors()
lbold = MyColors.lightColorsBold()

def game():
    name = input(lbold.LIGHT_greenBold("Your name: "))
    lbold.LIGHT_megantaBold("Welcome")
    lbold.LIGHT_redBold(pyfiglet.figlet_format(name))
    rand = random.randint(1 , 100)
    ranran = random.randrange(5 ,100 ,5)
    l = rand + rand
    lbiu.LIGHT_redBIU("\nThink a number")
    input(nbold.cyanBold("\nHit enter to continue! :"))
    p = l +ranran
    nbold.cyanBold(f"Add {ranran} in the number you've thought! ")
    input(lbold.LIGHT_megantaBold("Hit enter to continue! :"))
    p = p/2
    nbold.cyanBold(f"Divide the total bu 2! :")
    input(nbold.cyanBold("\nHit enter to continue! :"))

    p = p-rand
    lbold.LIGHT_greenBold(f"Sub {p} from lefted amount! ")
    input(nbold.cyanBold("\nHit enter to continue! :"))

    lbold.LIGHT_yellowBold(f"You are left with {p}")

no = ["n", "no"]
cont = ""

while cont not in no:
    game()

    cont = input(nbold.cyanBold("Do you want to play again!"))







