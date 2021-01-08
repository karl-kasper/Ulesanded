#KKO IT20
#Seiklusmäng
#10.12.2020
#Nimi
import os.path
from os import path
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
        gg = input("That character already exists. Would you like to overwrite it?(y/n)")
        if gg == "y":
            sav()
        else:
            print("I osa lõpp")
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
    else:
        print("Character wasn't saved.")
#Punktid
def skills():
    global hp
    global dmg
    global stm
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
        hp = input(f"Enter a number 1-{pnt} for HP:")
        while not hp.isdigit():
            hp = input(f"Please enter a NUMBER 1-{pnt} for HP: ")
        hp = int(hp)
        while hp>pnt:
            print(f"Can't spend more than {pnt}")
            hp = int(input(f"Enter a number 1-{pnt} for HP:"))
        pnt -= hp
    if pnt>0:
        dmg = input(f"Enter a number 1-{pnt} for damage:")
        while not dmg.isdigit():
            dmg = input(f"Please enter a NUMBER 1-{pnt}: ")
        dmg = int(dmg)
        while dmg>pnt:
            print(f"Can't spend more than {pnt}")
            dmg = int(input(f"Enter a number 1-{pnt}: "))
        pnt -= dmg
    if pnt>0:
        stm = input(f"Enter a number 1-{pnt} for stamina: ")
        while not stm.isdigit():
            stmn = input(f"Please enter a NUMBER 1-{pnt}: ")
        stm = int(stm)
        while stm>pnt:
            print(f"Can't spend more than {pnt}")
            stm = int(input(f"Enter a number 1-{pnt}: "))
        pnt -= stm
    #Base valued, et ükski 0 ei oleks
    stm += 25
    dmg += 5
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
#game() pole veel tähtis V
def game():
    print("You are in a dark room.")
    print("You feel a wooden object as you feel the area around you.")
    pick = input("Would you like to pick up the wooden object?(y/n) ")
    if pick == "y":
        print("You picked up a stick.")
        print("+1 atk")
        dmg += 1
        print(f"NOTE: Your damage is now {dmg}")
    elif pick == "n":
        print("You didn't pick up the wooden object.")
    else:
        print("You don't know what to do with the wooden object.") 
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
#Mäng
option()
