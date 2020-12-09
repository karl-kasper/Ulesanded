# K-KO IT20
# 24.11.2020
# Ülesanne 4
import random
#Ruudud ja kuubid
print("Arv Ruut Kuup")
for i in range(1,11):
    ruut = i*i
    kuup = i*i*i
    print(f"{i} {ruut:4} {kuup:5}")
input()
#Pank
print("****************")
print("******KPANK*****")
print("******€€€€******")
print("****************")
#andmed
aastad = 5
konto = 10000
intress = 0.05
print("Aasta Algsumma Intress Kokku")
for i in range(aastad):
    alg = konto
    konto = round(konto+(konto*intress))
    print(f"{i+1} {alg:10} {round(intress*alg):7} {konto:7}")
input()
#Arvamismäng
print("**********************")
print("******ARVAMISMÄNG*****")
print("******only 2.99€******")
print("**********************")
arvamised = 0
kordade_arv = 3
suvarv = random.randint(1,5)
while arvamised<kordade_arv:
    arvamised = arvamised+1
    arva = int(input("Arva ära arv vahemikus 1-5: "))
    if arva == suvarv:
        print("WIN")
        arvamised = 100
    else:
        print("Try again")
    if arvamised == kordade_arv:
        print("LOSE")
print("Game Over.")
input()
#Arvud 1-25 jaguvad 5
for i in range (1,101):
    if i%5==0:
        print(i)
#Korrutustabel
for i in range (1,11):
    print(f"5 x {i} = {5*i}")
#Paaris või paaritu
for i in range (1,10):
    if i%2:
        print(i,"-","paaritu")
    else:
        print(i,"-","paaris")
#Loto
print("Tänased lotonumbrid on: ", end="")
for i in range (5):
    suvarv = random.randint(0,9)
    print(suvarv, end="")
print("")
#Tärnid
#kahanev
mak = 6
for j in range (1,mak):
    print((mak-j)*"*")

#kasvav
for j in range (1,6):
    print("*"*j)

# tsükkel vahemikus 1-26
for i in range(1,26):
    #end määrab rea lõpu
    print("* ", end="")
    #leiab 5ga jagunevad arvud
    jaak = i%5
    if jaak==0:
        #lisab rea vahetuse
        print("",end="\n")
print("\n----- IF -----")
#Jalgpall
sugu = input("Sisesta sugu (m/n): ")
if sugu=="m":
    vanus = int(input("Sisesta vanus: "))
if sugu=="m" and vanus>=16 and vanus<=18:
    print("Sa kõlbad meeskonda")
elif sugu=="n":
    print("Sa kõlbad meeskonda")
else:
    print("Sa ei kõlba meeskonda, kuna sa pole piisavalt vana.")
#Müük
hind = int(input("Sisesta toote hind: "))
vahem = hind-hind*0.1
rohkem = hind-hind*0.2
if hind<=10:
    print("Toote hind on: ",vahem)
else:
    print("Toote hind on: ",rohkem)


#Juubel
sund = int(input("Sisesta sünniaasta: "))
vanus = 2020 - sund
jaak = vanus%5
if jaak==0:
    print("Sul on see aasta juubel")
else:
    print("Pole juubelit")
#Matemaatika
nr1 = int(input("Sisesta esimene arv: "))
nr2 = int(input("Sisesta teine arv: "))
tehe = input("Sisesta tehtemärk (+-*/): ")
if tehe == "+":
    v = nr1+nr2
elif tehe =="-":
    v = nr1-nr2
elif tehe =="*":
    v = nr1*nr2
else:
    v = nr1/nr2
print(f"{nr1}{tehe}{nr2}={v}")
#Ruut
Kulg1 = input("Sisesta esimene ruudu külg: ")
Kulg2 = input("Sisesta teine ruudu külg: ")
if Kulg1==Kulg2:
    print("Tegemist on ruuduga")
else:
    print("Tegemist ei ole ruuduga")