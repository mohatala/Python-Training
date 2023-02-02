from tkinter import *
import re
from tkinter.messagebox import *
import sqlite3



# Database
try:
    con = sqlite3.connect('DB.db')

    con.execute('''create table if not exists users(
                nom text not null,
                prenom text not null,
                email text not null,
                password text not null);      
    ''')
    con.close()

except Exception as ep:
    showerror('', ep)


def clear():
    nom.delete(0,END)
    pre.delete(0,END)
    em.delete(0,END)
    pwd.delete(0,END)

def create():
    try:
        con = sqlite3.connect('DB.db')
        c = con.cursor()
        c.execute("insert into users VALUES (:no, :p, :em, :p)",{
            'no': nom.get(),
            'p': pre.get(),
            'em': em.get(),
            'p': pwd.get()
            })
        con.commit()
        con.close()

    except Exception as Err:
        showerror('', Err)
       
   

def display():
    con = sqlite3.connect('DB.db')
    c = con.cursor()
    for row in c.execute("SELECT * FROM users"):
        showinfo("",row)
    con.close()

def connect():
    con = sqlite3.connect('DB.db')
    c = con.cursor()
    nom=""
    for row in c.execute("SELECT * FROM users where email=:lo and password=:pa",
                         {'lo':logtext.get(),
                          'pa':passtext.get()}):
        nom=row[0]
    if nom!="":
        #print(nom)
        Login.pack_forget()
        newuser.pack_forget()
        afterlogin.pack(expand=True)
    con.close()
    
   
ws = Tk()
ws.title('Application')
ws.geometry('500x400')
ws.config(bg="#447c84")
ws.attributes('-fullscreen',True)




def toframe2():
    Login.pack(expand=True)
    newuser.pack_forget()
    afterlogin.pack_forget()


def toframe1():
    newuser.pack(expand=True)
    Login.pack_forget()
    afterlogin.pack_forget()
   

# frames
newuser = Frame(ws, padx=20, pady=20)
Login = Frame(ws, padx=20, pady=20)
afterlogin = Frame(ws, padx=20, pady=20)


# labels
Label(newuser,text="Nouveau compte",font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

Label(newuser, text='Nom', font=("Times", "14")).grid(row=1, column=0, pady=5)


Label(newuser, text='Prénom', font=("Times", "14") ).grid(row=2, column=0, pady=5)

Label(newuser, text='Email Address', font=("Times", "14")).grid(row=3, column=0, pady=5)

Label(newuser, text='Password', font=("Times", "14")).grid(row=4, column=0, pady=5)



# Entry
nom = Entry(newuser, width=30)
nom.grid(row=1, column=1)

pre = Entry(newuser, width=30)
em = Entry(newuser, width=30)
pwd = Entry(newuser,show="*", width=30)

pre.grid(row=2, column=1)
em.grid(row=3, column=1)
pwd.grid(row=4, column=1)

# button
clr = Button(newuser, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=clear)
reg = Button(newuser, text="Créer le compte", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=create)
disp = Button(newuser, text="Display", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=display)


#------------------------------------------------------------------------------------------

Label(Login,text="Login").grid(row=1, column=0, pady=5)
logtext =Entry(Login, width = 15)
logtext.grid(row=2, columns=10, pady=5)

Label(Login,text="MP").grid(row=3, column=0, pady=5)
passtext =Entry(Login, width = 15)
passtext.grid(row=4, columns=10, pady=5)
b6 = Button(Login,text="OK",command=connect).grid(row=5, column=0, pady=5)
b5 = Button(Login,text="Exit",command=lambda:Login.pack_forget()).grid(row=5, column=6, pady=5)
#--------------------------------------------------------------------------------------------
Label(afterlogin,text="Frame2",font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

Label(afterlogin, text='-----Connection Reussi----', font=("Times", "14")).grid(row=1, column=0, pady=5)
#--------------------------------------------------------------------------------------------
fr2 = Button(ws, text="Se connecter", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=toframe2)

fr1 = Button(ws, text="Nouveau compte", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=toframe1)

exitapp = Button(ws,text="Quit",command=ws.destroy)
exitapp.place(x=200,y=10)


clr.grid(row=6, column=0, pady=20)
reg.grid(row=6, column=1, pady=20)
ext.grid(row=6, column=2, pady=20)
#disp.grid(row=7, column=1, pady=20)


fr2.pack(pady=20)
fr1.pack(pady=20)


ws.mainloop()
