# K-KO IT20
# Ül 6
# 02.12.2020

#faili avamine
minu_fail = open('deeza.txt', 'r')

#faili sisu lugemine
faili_sisu = minu_fail.readlines()

#faili sisu kuvamine
ref = 0
kesk = 0
erakondi = []
for i in range(len(faili_sisu)):
    enimi, pnimi, ek, sobrad = faili_sisu[i].split(" ")
    if ek == "RE":
        ref+=1
    elif ek == "KE":
        kesk+=1
    if ek not in erakondi:
        erakondi.append(ek)
    print(f"{enimi:11}{pnimi:10}{ek:4}{sobrad:5}", end="")
    #lisame andmed uude faili
    with open('deeza.txt', 'a') as fail_kirjutamiseks:
        fail_kirjutamiseks.write(enimi+" "+pnimi+"\n")
print(f"\n---------------\nReformikaid kokku: {ref}")
print(f"Kesikuid kokku: {kesk}")
print(f"Erakondi kokku: {len(erakondi)}")

#faili sulgemine
minu_fail.close