from tkinter import *
import random

#akna seaded
aken = Tk()
aken.title('Arvamismäng')
aken.iconbitmap('favicon.ico')
aken.geometry("400x250")
aken.resizable(0, 0)
#Tekst
tekst = Label(aken, text="Arva ära number 1-10",font="Tahoma 12", justify=CENTER)
tekst.grid(row=1, column=1,sticky=E+W)
sisestus = Entry(aken)
sisestus.grid(row=2,column=1,sticky=E+W)
def arva():
    number = int(random.randint(1,10))
    oigenumber="Õige number oli"+" "+str(number)
    sis=int(sisestus.get())
    if sis == number:
        tekst = Label(aken, text="Arvasid Õigesti!",font="Tahoma 12", justify=CENTER)
        tekst.grid(row=3, column=1,sticky=E+W)
        tekst = Label(aken, text=oigenumber,font="Tahoma 12", justify=CENTER)
        tekst.grid(row=4, column=1,sticky=E+W)
    else:
        tekst = Label(aken, text="Arvasid Valesti.",font="Tahoma 12", justify=CENTER)
        tekst.grid(row=3, column=1,sticky=E+W)
        tekst = Label(aken, text=oigenumber,font="Tahoma 12", justify=CENTER)
        tekst.grid(row=4, column=1,sticky=E+W)
nupp1 = Button(aken, text="OK",height=2, width=6, command=arva)
nupp1.grid(row=2, column=2)

aken.mainloop()
