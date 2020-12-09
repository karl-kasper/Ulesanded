# K-KO IT20
# 24.11.2020
# Ül 3
# Palindroom
def isPalindrome(s):
    return s == s[::-1]
s = input("Sisesta sõna: ")
ans = isPalindrome(s)
 
if ans:
    print(s,"on palindroom")
else:
    print(s,"ei ole palindroom")
# Tundide ajad
algus = input("Sisesta algusaeg (hh:mm): ")
lopp = input("Sisesta loppaeg (hh:mm): ")
hh1, mm1 = algus.split(":")
hh2, mm2 = lopp.split(":")
min1 = int(hh1)*60+int(mm1)
min2 = int(hh2)*60+int(mm2)
vahe = min2-min1
tund = vahe//60
minut = vahe%60
print(f"Päeva pikkus on {tund}:{minut}." )
# E-Mail
email = input("Sisesta email: ")
print("@" in email)
# Vandumine
lause = input("Ära siia vannu: ")
lause = (lause.lower()).replace("kurat","***")
print(lause)
# Korralik nimi
nimi = input("Sisesta nimi: ")
nimi = (nimi.strip()).capitalize()
print(nimi)
