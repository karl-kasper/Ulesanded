# KKO IT20
# Iseseisvad ülesanded 1
# 14.12.2020
import random
#Kolmnurgad
#A
for j in range(1,6):
    if j%2==0:
        print("", end="")
    else:
        print(j*"*")
for j in range (1,4):
    if j%2==0:
        print("", end="")
    else:
        print((4-j)*"*")
print("")
#B
for j in range (1,6):
    print((6-j)*"*")
print("")
#C
for j in range (1,6):
    print("*"*j)
print("")
#D
for j in range (1,6):
    print((6-j)*"*")
for j in range (1,5):
    print("*"*j)
#Lause tagurpidi
lause = input("Sisesta lause: ")
lause = lause.split()
lause.reverse()
lause = " ".join(lause)
print(lause)
#Takistus
#Jadamisi
R1 = int(input("Sisesta R1 takistus: "))
R2 = int(input("Sisesta R2 takistus: "))
R = R1+R2
print(f"Jadaühenduse kogutakistus on {R}")
#Rööp
R1 = int(input("Sisesta R1 takistus: "))
R1 = 1/(R1)
R2 = int(input("Sisesta R2 takistus: "))
R2 = 1/(R2)
R = 1/(R1+R2)
print(f"Rööpühenduse kogutakistus on {R}")
#Lipp
print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\n==============================================\n==============================================\n==============================================\n==============================================\n----------------------------------------------\n----------------------------------------------\n----------------------------------------------\n----------------------------------------------")
#Liitmine
a1 = int(input("Sisesta esimene arv: "))
a2 = int(input("Sisesta teine arv: "))
print(f"Nende arvude summa on {a1+a2}")