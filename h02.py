import os
os.system('cls')
import math
#Kütusekulu
kutus = int(input("Sisesta kütuse kogus liitrites: "))
kaugus = int(input("Sisesta vahemaa liitrites: "))
print(kutus/(kaugus/100))
#Arvusüsteemid
arv = int(input("Sisesta 10ndarv: "))
binary = bin(arv)
hexa = hex(arv)
octa = oct(arv)
print("Arv 2ndsüsteemis",binary)
print("Arv 8ndsüsteemis",octa)
print("Arv 16ndsüsteemis",hexa)
#Aja teisendus 72
aeg = int(input("Sisesta aeg minutites: "))
h = aeg//60
m = aeg%60
print(aeg,"minutit on",h,":",m)

#Leia kolmnurga hüpotenuus
a,b = 16,9
c = math 
