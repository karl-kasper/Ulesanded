#KKO IT20
#Ülesanne 8
#09.12.2020
class Auto:
    #atribuudid
    nimi = ""
    aasta = 0
    hind = 0
    
    #meetodid
    def __init__(self,x,y,z,v,c):
        self.mark = x
        self.aasta = y
        self.hind = z
        self.varv = v
        self.kiirus = c
    
    def lisamark(self,x):
        self.mark = x
        
    def lisaaasta(self,y):
        self.aasta = y
        
    def lisahind(self,z):
        self.hind = z
        
    def lisavarv(self,v):
        self.varv = v
        
    def lisakiirus(self,c):
        self.kiirus = c
        
    def kuva(self):
        print(f"Mark: {self.mark}\nAasta: {self.aasta}\nHind: {self.hind}\nVärv: {self.varv}\nMaksimum kiirus: {self.kiirus}")
minuAuto = Auto("Toyota", 1991, "2000€", "Kollane", "20KM/H")
minuAuto.kuva()