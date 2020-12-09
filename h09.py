#KKO IT20
#Ülesanne 9
#09.12.2020

ik = input("Sisesta isikukood: ")
if len(ik)==11:
    p = ik[5:7]
    k = ik[3:5]
    a = ik[1:3]
    print(f"{p}.{k}.{a}")