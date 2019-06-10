from os import system, name
from time import sleep
import random

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

name = ("    1        2        3     ")
cup1 = ("   ___      ___      ___    ")
cup2 = ("  #   #    #   #    #   #   ")
cup3 = (" #     #  #     #  #     #  ")
cup4 = (" -------  -------  -------  ")

while 1:
    clear()
    print(" The coin lies in the middle of the cup and is shuffled....")
    print(name)
    print(cup1)
    sleep(1)
    print(cup2)
    sleep(1)
    print(cup3)
    sleep(1)
    print(cup4)
    sleep(2)

    coin = random.randint(1, 3)
    user =  int(input("Enter the number of the cup where the coin lies in: "))

    sleep(1.5)
    if user == coin:
        print("Yes the coin lies in cup {0}".format(coin))
    else:
        print("Sorry the coin lies in cup {0}".format(coin))

    sleep(3)

    cont = input("Do you want to continue the game?(y/n): ")
    if cont == "n":
        quit()
