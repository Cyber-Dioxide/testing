import random
import pyfiglet
import MyColors


lbiu = MyColors.lightColorsBIU()
nbiu = MyColors.NormalBIUColors()

nbold = MyColors.NormalBoldColors()
nbold = MyColors.lightColorsBold()

def game():
    name = input(nbold.LIGHT_greenBold("Your name: "))
    nbold.LIGHT_greenBold("Welcome")
    nbold.LIGHT_cyanBold(pyfiglet.figlet_format(name))
    rand = random.randint(1 , 100)
    ranran = random.randrange(5 ,100 ,5)
    l = rand + rand
    lbiu.LIGHT_redBIU("\nThink a number")
    input(nbold.LIGHT_cyanBold("\nHit enter to continue! :"))
    p = l +ranran
    nbold.LIGHT_cyanBold(f"Add {ranran} in the number you've thought! ")
    input(nbold.LIGHT_megantaBold("Hit enter to continue! :"))
    p = p/2
    nbold.LIGHT_cyanBold(f"Divide the total bu 2! :")
    input(nbold.LIGHT_cyanBold("\nHit enter to continue! :"))

    p = p-rand
    nbold.LIGHT_greenBold(f"Sub {p} from lefted amount! ")
    input(nbold.LIGHT_cyanBold("\nHit enter to continue! :"))

    nbold.LIGHT_yellowBold(f"You are left with {p}")

no = ["n", "no"]
cont = ""

while cont not in no:
    game()

    cont = input(nbold.LIGHT_cyanBold("Do you want to play again!"))







