#KKO IT20
#Seiklusmäng
#10.12.2020
#Nimi
import time
import random
import os.path
from os import path
#Mäng
def game(d,h,s,sc):
    score=sc
    dmg=d
    hp=h
    stm=s
    enhp = 100
    print("You are in a dark room.")
    time.sleep(2)
    print("You feel a wooden object as you feel the area around you.")
    time.sleep(1)
    pick = input("Would you like to pick up the wooden object?(y/n) ")
    if pick == "y":
        time.sleep(1)
        print("You picked up a stick.")
        print("+1 atk")
        dmg += 1
        time.sleep(1)
        print(f"NOTE: Your damage is now {dmg}")
    elif pick == "n":
        time.sleep(1)
        print("You didn't pick up the wooden object.")
    else:
        time.sleep(1)
        print("You don't know what to do with the wooden object.")
    time.sleep(1)
    print("You move forward until you reach a forest.")
    time.sleep(1)
    print("There's a goblin in the distance.")
    time.sleep(1)
    approach = input("Approach it to battle it?(y/n)")
    if approach == "y":
        time.sleep(1)
        print("You approach the goblin")
        time.sleep(1)
        battle(dmg,hp,stm,enhp,sc)
        return enhp
def savting():
    f = open(f"{character}.txt", "w+")
    f.write(f"Character's name: {character}.\nSkillpoints:\n HP: {hp}\n Damage: {dmg}\n Stamina: {stm}\n Score: {sc}")
    f.close
def load():
    f = open(f'{character}.txt', 'r')
    content = f.read()
    print(content)
    f.close()
    game(dmg,hp,stm,sc)
def name():
    #Võtab nime ja paneb suure algustähe
    global character
    character = input("Enter a name for your character: ")
    character = character.capitalize()
    print(f"Your name is {character}.\n")
#Tegelase salvestus
def saving():
    #Vaatab kas sellise nimega tegelane juba olemas, kui on siis küsib kas tahad üle kirjutada.
    ball = str(path.exists(f'{character}.txt'))
    if ball == "True":
        gg = input("That character already exists. Would you like to load it?(y/n)")
        if gg == "y":
            load()
        else:
            print("Using new character without saving.")
            game(dmg,hp,stm,sc)
    else:
        sav()
    #Salvestamine teksitifaili
def sav():
    save = input("Save character?(y/n)")
    if save == "y":
        #tekitab tekstifaili tegelase nimega sinna kus on skriptifail, kui olemas siis tahtmise korral kirjutab üle
        f = open(f"{character}.txt", "w+")
        f.write(f"Character's name: {character}.\nSkillpoints:\n HP: {hp}\n Damage: {dmg}\n Stamina: {stm}")
        f.close
        print("Character was saved.")
        game(dmg,hp,stm,sc)
    else:
        print("Character wasn't saved.")
        game(dmg,hp,stm,sc)
#Punktid
def skills():
    global hp
    global dmg
    global stm
    global sc
    sc=0
    pnt = 10
    hp = 0
    dmg = 0
    stm = 0
    print("You have 10 skillpoints.")
    print("1. HP")
    print("2. Damage")
    print("3. Stamina")
    #Küsib kasutajalt koguse ja vaatab kas number sobib, kui sobib lisab võimele
    if pnt>0:
        hp = input(f"Enter a number 0-{pnt} for HP:")
        while not hp.isdigit():
            hp = input(f"Please enter a NUMBER 0-{pnt} for HP: ")
        hp = int(hp)
        while hp>pnt:
            print(f"Can't spend more than {pnt}")
            hp = int(input(f"Enter a number 0-{pnt} for HP:"))
        pnt -= hp
    if pnt>0:
        dmg = input(f"Enter a number 0-{pnt} for damage:")
        while not dmg.isdigit():
            dmg = input(f"Please enter a NUMBER 0-{pnt}: ")
        dmg = int(dmg)
        while dmg>pnt:
            print(f"Can't spend more than {pnt}")
            dmg = int(input(f"Enter a number 0-{pnt}: "))
        pnt -= dmg
    if pnt>0:
        stm = input(f"Enter a number 0-{pnt} for stamina: ")
        while not stm.isdigit():
            stmn = input(f"Please enter a NUMBER 0-{pnt}: ")
        stm = int(stm)
        while stm>pnt:
            print(f"Can't spend more than {pnt}")
            stm = int(input(f"Enter a number 0-{pnt}: "))
        pnt -= stm
    #Base valued, et ükski 0 ei oleks
    stm += 25
    dmg += 500000
    hp += 100
    #Lisab ülejäänud punktid viimasele 
    if pnt>0:
        print("The rest of the skillpoints were added to the final skill automatically")
        stm = pnt
        stm += 25
    print(f"HP: {hp}")
    print(f"Damage: {dmg}")
    print(f"Stamina: {stm}")
    saving()
    return [dmg,hp,stm,sc]
def option():
    #Küsib kuni saab normaalse vastuse
    start = input("Would you like to start the game?(y/n): ")
    yes = 0
    while yes == 0:
        if start == "y":
            name()
            skills()
            yes = yes+1
        elif start == "n":
            print("Ok")
            yes = yes+1
        else:
            print("What")
            start = input("Would you like to start the game?(y/n): ")
def battle(dmg,hp,stm,enhp,sc):
    while hp>=0 and enhp>=0:
        print("Options\n1. Attack\n2. Heal")
        opt = input("What will you do?")
        if opt == "1" or opt=="attack":
            crit = random.randint(1,5)
            if crit == 3:
                print(f"You got a crit doing double damage!")
                enhp-=dmg*2
                print(enhp)
                print(f"Goblin's hp is now {enhp}")
                time.sleep(1)
            else:
                print(f"You attack the goblin doing {dmg} damage")
                enhp-=dmg
                print(enhp)
                print(f"Goblin's hp is now {enhp}")
                time.sleep(1)
        elif opt == "2" or opt=="heal":
            heal = random.randint(10,30)
            print("You heal yourself")
            hp+=heal
            print(f"You got {heal} extra health.")
            print(f"Your hp is now {hp}")
        if enhp>=0:
            endmg = random.randint(10,25)
            time.sleep(1)
            print(f"The goblin attacks you doing {endmg} damage!")
            hp-=endmg
            print(f"Your hp is now {hp}")
            time.sleep(1)
    if hp<=0:
        print(f"You lost the game.")
        print("Your score:{sc}")
        savting()
    else:
        print("You won the battle!")
        sc+=10
        print(f"Your score is now: {sc}")
        savting()
#Mäng
option()
