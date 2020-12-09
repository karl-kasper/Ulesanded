#Rühm 1
#is.ülesanded 1-2
import random
#Jukebox
fail = input("Sisesta failinimi koos laiendiga: ")
nr = 1
playlist = open(fail)
for i in playlist:
    print(str(nr)+". ",i,end="")
    nr += 1
lugu = int(input("\n\nMitmendat lugu tahad? "))
nr=1
playlist = open(fail)
for i in playlist:
    if nr==lugu:
        print(f"Mängitav muusikapala on {i}.")
    nr+=1
input()
#Sissetulekud
fail = open("konto.txt")
for i in fail:
    if float(i) > 0:
        print(i,end="")
#Jänesevanemate mure v3
ringid = abs(int(input("Sisesta ringide arv: ")))
porgandid = 0
for i in range(1,ringid+1):
    if i%2 == 0:
        porgandid += i
print(f"Saadavate porgandite koguarv on {porgandid}.")
#Ülikooli vastuvõetud
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()
aasta = int(input("Sisesta aasta: "))
print(f"Aastal {aasta} võeti vastu {vastuvõetud[aasta-2011]} õpilast.")
#Õunad
ounad = 14
mitu = int(input("Sisesta tahtjate arv: "))
for i in range(mitu):
    oun = random.randint(1,2)
    ounad=ounad-oun
    print(oun)
print(f"Lumivalgekesele jääb: {ounad}")
#Täringud
taringute_arv = int(input("Täringute arv: "))
for i in range(taringute_arv):
    print(random.randint(1,6))
#Lapsevanemad
ringide_arv = abs(int(input("Sisestage ringide arv: ")))
porgandid = 0
ring = 1
while ringide_arv>=ring:
    if ring&1 == 0:
        porgandid+=ring
    ring+=1
print(porgandid)
    
#Äratus
korda = int(input("Mitu korda kell heliseb: "))
for i in range(korda):
    print("Tõuse ja sära!")
#Bussid
in_arv = int(input("Sisestage inimeste arv: "))
kht_arv = int(input("Sisestage kohtade arv: "))
if in_arv%kht_arv == 0:
    print(in_arv//kht_arv)
else:
    print(in_arv//kht_arv+1)
print(f"Viimases bussis on {in_arv%kht_arv} inimest.")
input()
#Pilved
korgus = float(input("Sisesta pilvede kõrgus: "))
if korgus > 6:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")
#Aasta liblikas
aasta = 2020
liblikas = "teelehemosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas
print(lause)
#Tervitus

print("Tere, maailm!")