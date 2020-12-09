# KKO IT20
# Is. töö 4
# 09.12.2020
#Tervitused
def tervitus(n):
    print(f"Võõrustaja : \"Tere!\"\nTäna {n}. kord tervitada, mõtiskleb võõrustaja.\nKülaline: \"Tere, suur tänu kutse eest!\"")

n = int(input("Sisestage külaliste arv: "))
for i in range(n):
    tervitus(i+1)
#Pidu
def eelarve(kutsutud, tuleb):
    maxi = round((kutsutud*10)*55)
    mini = round((tuleb*10)*55)
    return [maxi, mini]
kutsutud = int(input("Mitu inimest kutsuti? "))
tuleb = int(input("Mitu inimest tuleb? "))
list = eelarve(kutsutud, tuleb)
print(f"Maksimum eelarve: {list[0]}€")
print(f"Miinimum eelarve: {list[1]}€")
#Õunamahl
def mahlapakkide_arv(kogus):
    mahlapakkidearv = round(kogus * 0.4/3,0)
    return int(mahlapakkidearv)
kogus = int(input("Sisesta õunte kogus kg: "))
print(mahlapakkide_arv(kogus))
#Bänner1
def banner(t):
    return t.upper()

korda = int(input("Mitu korda reklaamlauset kuvatakse? "))
b = input("Sisesta reklaamlause: ")

for i in range(korda):
    print(banner(b))
#Bänner2
def banner():
    nuts = input("Sisesta bänner: ")
    kord = abs(int(input("Sisesta mitu korda bännerit väljastada: ")))
    for i in range(kord):
        print(nuts.upper())
banner()