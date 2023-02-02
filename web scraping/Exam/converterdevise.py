from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *

def Eurotodhs():
    euro=txteuro.get()
    dh=float(euro)*11.5
    lblDHS=Label(w,text=dh)
    lblDHS.place(x=350,y=20)

def DHStoEuro():
    dh=txtDHS.get()
    euro=float(dh)/11.5
    lblEuro=Label(w,text=euro)
    lblEuro.place(x=350,y=50)
    
w = Tk()
w.title("Convert")

w.geometry("450x200")
style = Style()
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'blue')
lbl1=Label(w,text="Euro")
lbl1.place(x=20,y=20)

txteuro=Entry(w)
txteuro.place(x=100,y=20)

Eurobtn=Button(w,text="Euro=>DHS",command=Eurotodhs)
Eurobtn.place(x=250,y=20)


lbl1=Label(w,text="DHS")
lbl1.place(x=20,y=50)
txtDHS=Entry(w)
txtDHS.place(x=100,y=50)

DHSbtn=Button(w,text="DHS=>Euro",command=DHStoEuro)
DHSbtn.place(x=250,y=50)



close=Button(w,text="Fermer",command=w.destroy)
close.place(x=250,y=80)



