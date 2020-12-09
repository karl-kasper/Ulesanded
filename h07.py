# K-KO IT20
# Ülesanne 7
# 02.12.2020
#Ruumala

def minuApp():
    print("***********Ruumala leidmine***********")
    print("Vali kujund\n0 Sulge programm\n1 Kuup\n2 Kera\n3 Koonus\n4 Silinder")
    print("**************************************")
    valik = int(input("Sisesta soovitud kujundi number: "))
    if valik==1:
        print(f"Kuubi ruumala on: {kuup()}")
    elif valik==2:
        print(f"Kera ruumala on: {kera()}")
    elif valik==3:
        print(f"Koonus ruumala on: {koonus()}")
    elif valik==4:
        print(f"Silinder ruumala on: {silinder()}")
    elif valik>4:
        print("Sellist valikut pole")
    else:
        return valik
def kuup():
    print("Leian kuubi")
    x = int(input("Sisesta külg 1: "))
    y = int(input("Sisesta külg 2: "))
    z = int(input("Sisesta külg 1: "))
    v = x * y * z
    return v
def kera():
    print("Leian kera")
    r = int(input("Sisesta kera raadius: "))
    v = 4/3*3.14*pow(r,3)
    return v
def koonus():
    print("Leian koonuse")
    v = 
def silinder():
    print("Leian silindri")
loop = 1
while loop==1:
    v = minuApp()
    if v==0:
        loop=0
print("Programmi lõpp")
#funktsiooni loomine
mis = input("Sisesta keel(en,et,ge): ")
def tervita(keel="ge"):
    "Tervitab keele järgi"
    if keel=="et":
        nimi = input("Sisesta oma nimi: ")
        return "Tervist, "+nimi+"!"
    elif keel=="en":
        nimi = input("Enter your name: ")
        return "Hi, "+nimi+"!"
    else:
        nimi = input("Gib deinen Namen: ")
        return "Hallo, "+nimi+"!"
print(tervita(mis))
