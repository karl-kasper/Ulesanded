# K-KO IT20
# 25.11.2020
# Ülesanne 5
#Tärnid
v = [23,17,26,39,9,28]
for i in range(len(v)):
    print(v[i]*"*")
#Vanused
v = [23,17,26,39,9,28]
suurim = max(v)
vaikseim = min(v)
summa = sum(v)
keskmine = summa/len(v)
print(f"Suurim: {suurim} \nväikseim: {vaikseim} \nsumma: {summa} \nkeskmine: {keskmine}")
input()
#Duplikaadid
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
uus_opilased = []
#kui olemas ei lisa
for i in range(len(opilased)):
    if opilased[i] not in uus_opilased:
        uus_opilased.append(opilased[i])
    else:
        print(f"Leiti kordus {opilased[i]}")
input()

#Õpilaste nimede muutmine
opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
    #Õpilaste nimed numbriga
for i in range (len(opilased)):
    print(f"{i+1}. {opilased[i]}")
#küsin kasutajalt, mitmendat nime soovib muuta
arv = int(input("Mitmendat nime soovid muuta: "))
#tagasiside
print(f"Te soovite muuta nime: {opilased[arv-1]}")
#küsin asendavat nime
nimi = input("Millise nimega soovid asendada: ")
#kustutan kasutaja valitud valiku
del opilased[arv-1]
opilased.insert(arv-1, nimi)
print("Uus nimekiri")
for i in range (len(opilased)):
    print(f"{i+1}. {opilased[i]}")
input()



#Nimede lisamine massiivi
nimed = []


for i in range(5):
    #küsib nime
    nimi = input("Sisesta nimi: ")
    #lisab nime loendisse
    nimed.append(f"Viimati lisatud nimi {nimi}")
    #näitan lisatud nime
print(nimi)
nimed.sort()
    