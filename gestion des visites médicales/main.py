import tkinter as tk
from tkinter import *
import re
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
from tkcalendar import Calendar

conn=sqlite3.connect("C:/Users/21260/Desktop/Master/Python/gestion des visites médicales/Cabinet_Medicale.db")
c=conn.cursor()
query = "SELECT * FROM MEDECIN"
c.execute(query)
resultMed = c.fetchall()
query = "SELECT * FROM Patient"
c.execute(query)
resultPat = c.fetchall()
idx=0
idp=0
def Medecin():
    framePatient.pack_forget()
    frameConsultation.pack_forget()
    framemedecin.pack(expand=True)
    Login.pack_forget()
    newuser.pack_forget()
   

def Patient():
    framemedecin.pack_forget()
    frameConsultation.pack_forget()
    framePatient.pack(expand=True)
    Login.pack_forget()
    newuser.pack_forget()

def Consultation():
    Login.pack_forget()
    newuser.pack_forget()
    framemedecin.pack_forget()
    framePatient.pack_forget()
    frameConsultation.pack(expand=True)
def toframe2():
    Login.pack(expand=True)
    newuser.pack_forget()
    framemedecin.pack_forget()
    frameConsultation.pack_forget()
    framePatient.pack_forget()


def toframe1():
    newuser.pack(expand=True)
    Login.pack_forget()
def clear():
    username.delete(0,END)
    pwd.delete(0,END)

def create():
    try:
        #con = sqlite3.connect('C:/Users/21260/Desktop/Master/Python/gestion des visites médicales/Cabinet_Medicale.db')
        #c1 = con.cursor()
        c.execute("insert into USERS VALUES (null,:no, :p)",{
            'no': username.get(),
            'p': pwd.get()
            })
        conn.commit()
        showinfo("Enregistrer","Enregistrer")
        #c.close()

    except Exception as Err:
        showerror('', Err)
       

def connect():
    #con = sqlite3.connect('DB.db')
    #c = con.cursor()
    nom=""
    for row in c.execute("SELECT * FROM USERS where Username=:lo and Password=:pa",
                         {'lo':logtext.get(),
                          'pa':passtext.get()}):
        nom=row[0]
    if nom!="":
        #print(nom)
        Login.pack_forget()
        newuser.pack_forget()
        ok=1
        frameConsultation.pack(expand=True)
    #c.close()
    
   
##########################################
def firstitem():
    global idx
    idx=0
    txtmat.delete(0, END)
    txtnom.delete(0, END)
    txtadr.delete(0, END)
    txtspec.delete(0, END)
    txtmat.insert(0,resultMed[idx][0])
    txtnom.insert(0,resultMed[idx][1])
    txtadr.insert(0,resultMed[idx][2])
    txtspec.insert(0,resultMed[idx][3])
def lastitem():
    global idx
    idx=len(resultMed)-1
    txtmat.delete(0, END)
    txtnom.delete(0, END)
    txtadr.delete(0, END)
    txtspec.delete(0, END)
    txtmat.insert(0,resultMed[idx][0])
    txtnom.insert(0,resultMed[idx][1])
    txtadr.insert(0,resultMed[idx][2])
    txtspec.insert(0,resultMed[idx][3])
def nextitem():
    global idx
    idx=idx+1
    if(idx==len(resultMed)):
        showinfo("message","Last Row")
    else:
         txtmat.delete(0, END)
         txtnom.delete(0, END)
         txtadr.delete(0, END)
         txtspec.delete(0, END)
         txtmat.insert(0,resultMed[idx][0])
         txtnom.insert(0,resultMed[idx][1])
         txtadr.insert(0,resultMed[idx][2])
         txtspec.insert(0,resultMed[idx][3])
        
def backitem():
    global idx
    idx=idx-1
    if(idx==-1):
        showinfo("message","First Row")
    else:
         txtmat.delete(0, END)
         txtnom.delete(0, END)
         txtadr.delete(0, END)
         txtspec.delete(0, END)
         txtmat.insert(0,resultMed[idx][0])
         txtnom.insert(0,resultMed[idx][1])
         txtadr.insert(0,resultMed[idx][2])
         txtspec.insert(0,resultMed[idx][3])
##########################################
def firstitempatient():
    global idp
    idp=0
    txtmatp.delete(0, END)
    txtnomp.delete(0, END)
    txtadrp.delete(0, END)
    txtdn.delete(0, END)
    txtprenomp.delete(0, END)
    txtmatp.insert(0,resultPat[idp][0])
    txtnomp.insert(0,resultPat[idp][1])
    txtprenomp.insert(0,resultPat[idp][2])
    txtadrp.insert(0,resultPat[idp][3])
    txtdn.insert(0,resultPat[idp][4])

def lastitempatient():
    global idp
    idp=len(resultPat)-1
    txtmatp.delete(0, END)
    txtnomp.delete(0, END)
    txtadrp.delete(0, END)
    txtdn.delete(0, END)
    txtprenomp.delete(0, END)
    txtmatp.insert(0,resultPat[idp][0])
    txtnomp.insert(0,resultPat[idp][1])
    txtprenomp.insert(0,resultPat[idp][2])
    txtadrp.insert(0,resultPat[idp][3])
    txtdn.insert(0,resultPat[idp][4])
def nextitempatient():
    global idp
    idp=idp+1
    if(idp==len(resultPat)):
        showinfo("message","Last Row")
    else:
         txtmatp.delete(0, END)
         txtnomp.delete(0, END)
         txtadrp.delete(0, END)
         txtdn.delete(0, END)
         txtprenomp.delete(0, END)
         txtmatp.insert(0,resultPat[idp][0])
         txtnomp.insert(0,resultPat[idp][1])
         txtprenomp.insert(0,resultPat[idp][2])
         txtadrp.insert(0,resultPat[idp][3])
         txtdn.insert(0,resultPat[idp][4])
        
def backitempatient():
    global idp
    idp=idp-1
    if(idp==-1):
        showinfo("message","First Row")
    else:
         txtmatp.delete(0, END)
         txtnomp.delete(0, END)
         txtadrp.delete(0, END)
         txtdn.delete(0, END)
         txtprenomp.delete(0, END)
         txtmatp.insert(0,resultPat[idp][0])
         txtnomp.insert(0,resultPat[idp][1])
         txtprenomp.insert(0,resultPat[idp][2])
         txtadrp.insert(0,resultPat[idp][3])
         txtdn.insert(0,resultPat[idp][4])
##################################Medecin############################
def insertmedecin():
    print(txtmat.get())
    liste=[(int(txtmat.get()),txtnom.get(),txtadr.get(),txtspec.get())]
    c.executemany("INSERT INTO MEDECIN VALUES (?,?,?,?)",liste)
    conn.commit()
    showinfo("message","Insert succesfuly")
def modifiermedecin():
    liste=[(txtnom.get(),txtadr.get(),txtspec.get(),int(txtmat.get()))]
    c.executemany("UPDATE MEDECIN SET NOM_MEDECIN=? ,ADR_MEDECIN=?,SPECIALITE=? WHERE NUM_MATRICULE=?",liste)
    conn.commit()
    showinfo("message","Updated succesfuly")

def Deletemedecin():
    liste=[(int(txtmat.get()))]
    c.execute("DELETE FROM MEDECIN WHERE NUM_MATRICULE=?",liste)
    conn.commit()
    showinfo("message","Deleted succesfuly")
#####################################Patient################################3333
def insertpatient():
    liste=[(int(txtmatp.get()),txtnomp.get(),txtprenomp.get(),txtadrp.get(),txtdn.get())]
    print(txtmat.get())
    c.executemany("INSERT INTO PATIENT VALUES (?,?,?,?,?)",liste)
    conn.commit()
    showinfo("message","Insert succesfuly")
def modifierpatient():
    liste=[(txtnomp.get(),txtprenomp.get(),txtadrp.get(),txtdn.get(),int(txtmatp.get()))]
    c.executemany("UPDATE PATIENT SET NOM_PAT=? ,PRENOM_PAT=?,ADR_PAT=?,DATE_NAISS=? WHERE NUM_SEC_SOCIALE=?",liste)
    conn.commit()
    showinfo("message","Updated succesfuly")

def Deletepatient():
    liste=[(int(txtmatp.get()))]
    c.execute("DELETE FROM PATIENT WHERE NUM_SEC_SOCIALE=?",liste)
    conn.commit()
    showinfo("message","Deleted succesfuly")
#######################Consultation###########################3
def Save():
    me=selected_med.get().split()
    pa=selected_pat.get().split()
    liste=[(int(me[0]),int(pa[0]),cal.get_date())]
    c.executemany("INSERT INTO CONSULTATION VALUES (?,?,?)",liste)
    conn.commit()
    showinfo("message","Rendez Vous Enregistrer")

#############################################
w = Tk()
w.title("Interface")
w.geometry("700x400")
##########################


menu = Menu(w)
w.config(menu=menu)

fileMenu = Menu(menu)
fileMenu.add_command(label="Se connecter", command=toframe2)
fileMenu.add_command(label="Nouveau compte", command=toframe1)
fileMenu.add_command(label="Exit", command=w.quit)
menu.add_cascade(label="File", menu=fileMenu)

editMenu = Menu(menu)

editMenu.add_command(label="Medecin" , command=Medecin)
editMenu.add_command(label="Patient", command=Patient)
editMenu.add_command(label="Consultation", command=Consultation)
menu.add_cascade(label="Edition", menu=editMenu)

############## Gestion Medecin########################
framemedecin = Frame(w, padx=40, pady=40)
lbl=Label(framemedecin,text="Ajouter Medecin",font=("Times", "24", "bold")).grid(row=0, column=0, pady=2)

lbl1=Label(framemedecin,text="Matricule",font=("Times", "14")).grid(row=1, column=0, pady=2)
txtmat=Entry(framemedecin)
txtmat.grid(row=1, column=2, pady=1)
lbl2=Label(framemedecin,text="Nom",font=("Times", "14")).grid(row=2, column=0, pady=2)
txtnom=Entry(framemedecin)
txtnom.grid(row=2, column=2, pady=1)
lbl3=Label(framemedecin,text="Adresse",font=("Times", "14")).grid(row=4, column=0, pady=2)
txtadr=Entry(framemedecin)
txtadr.grid(row=4, column=2, pady=1)
lbl4=Label(framemedecin,text="Specialite",font=("Times", "14")).grid(row=5, column=0, pady=2)
txtspec=Entry(framemedecin)
txtspec.grid(row=5, column=2, pady=1)

btn1=Button(framemedecin,text="<<",command=firstitem).grid(row=6, column=0, pady=1)
btn2=Button(framemedecin,text="<",command=backitem).grid(row=6, column=1, pady=1)
btn3=Button(framemedecin,text=">",command=nextitem).grid(row=6, column=2, pady=1)
btn4=Button(framemedecin,text=">>",command=lastitem).grid(row=6, column=3, pady=1)

insert=Button(framemedecin,text="Insert",width=20,command=insertmedecin).grid(row=9, column=0, pady=1)
impor=Button(framemedecin,text="Delete",width=20,command=Deletemedecin).grid(row=9, column=2, pady=1)
modif=Button(framemedecin,text="Update",width=20,command=modifiermedecin).grid(row=9, column=4, pady=1)
############## Gestion Patient########################
framePatient = Frame(w, padx=40, pady=40)
Label(framePatient,text="Nouveau Patient",font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)
lbl1=Label(framePatient,text="Num Securite Social",font=("Times", "14")).grid(row=1, column=0, pady=2)
txtmatp=Entry(framePatient)
txtmatp.grid(row=1, column=2, pady=1)
lbl2=Label(framePatient,text="Nom",font=("Times", "14")).grid(row=2, column=0, pady=2)
txtnomp=Entry(framePatient)
txtnomp.grid(row=2, column=2, pady=1)
lbl5=Label(framePatient,text="Prenom",font=("Times", "14")).grid(row=3, column=0, pady=2)
txtprenomp=Entry(framePatient)
txtprenomp.grid(row=3, column=2, pady=1)
lbl3=Label(framePatient,text="Adresse",font=("Times", "14")).grid(row=5, column=0, pady=2)
txtadrp=Entry(framePatient)
txtadrp.grid(row=5, column=2, pady=1)
lbl4=Label(framePatient,text="Date Naissance",font=("Times", "14")).grid(row=6, column=0, pady=2)
txtdn=Entry(framePatient)
txtdn.grid(row=6, column=2, pady=1)

btn1=Button(framePatient,text="<<",command=firstitempatient).grid(row=8, column=0, pady=1)
btn2=Button(framePatient,text="<",command=backitempatient).grid(row=8, column=1, pady=1)
btn3=Button(framePatient,text=">",command=nextitempatient).grid(row=8, column=2, pady=1)
btn4=Button(framePatient,text=">>",command=lastitempatient).grid(row=8, column=3, pady=1)

insert=Button(framePatient,text="Insert",width=20,command=insertpatient).grid(row=11, column=0, pady=1)
impor=Button(framePatient,text="Delete",width=20,command=Deletepatient).grid(row=11, column=2, pady=1)
modif=Button(framePatient,text="Update",width=20,command=modifierpatient).grid(row=11, column=4, pady=1)

############## Gestion Consultation########################
frameConsultation = Frame(w, padx=40, pady=40)
Label(frameConsultation,text="Nouveau Consultation",font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

lbl1=Label(frameConsultation,text="Choisie Medecin:",font=("Times", "14")).grid(row=1, column=0, pady=2)
selected_med = tk.StringVar()
med_cb = ttk.Combobox(frameConsultation, textvariable=selected_med)
l=[]
for i in resultMed:
     l.append(str(i[0])+' '+i[1]+' '+i[2])

med_cb['values'] =l
med_cb['state'] = 'readonly'
med_cb.grid(row=1, column=2, pady=1)

lbl2=Label(frameConsultation,text="Choisie Patient:",font=("Times", "14")).grid(row=2, column=0, pady=2)
selected_pat = tk.StringVar()
pat_cb = ttk.Combobox(frameConsultation, textvariable=selected_pat)
l2=[]
for i in resultPat:
     l2.append(str(i[0])+' '+i[1]+' '+i[2])

pat_cb['values'] = l2
pat_cb['state'] = 'readonly'
pat_cb.grid(row=2, column=2, pady=1)

lbl5=Label(frameConsultation,text="Choisie la Date:",font=("Times", "14")).grid(row=3, column=0, pady=2)
cal = Calendar(frameConsultation, selectmode = 'day',year = 2022, month = 12,day = 13)
cal.grid(row=3, column=2, pady=1)

Enregistrer=Button(frameConsultation,text="Enregistrer",width=30,font=("Times", "14", "bold"),command=Save).grid(row=5, column=2, pady=1)
##########################################
#########################Login########################33
# frames
newuser = Frame(w, padx=20, pady=20)
Login = Frame(w, padx=20, pady=20)
# labels
Label(newuser,text="Nouveau compte",font=("Times", "24", "bold")).grid(row=0, columnspan=3, pady=10)

Label(newuser, text='USER Name', font=("Times", "14")).grid(row=1, column=0, pady=5)

Label(newuser, text='Password', font=("Times", "14")).grid(row=4, column=0, pady=5)

# Entry
username = Entry(newuser, width=30)
username.grid(row=1, column=1)
pwd = Entry(newuser,show="*", width=30)
pwd.grid(row=4, column=1)

# button
clr = Button(newuser, text="Clear", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=clear)
reg = Button(newuser, text="Créer le compte", padx=20, pady=10, relief=SOLID, font=("Times", "14", "bold"), command=create)
clr.grid(row=6, column=0, pady=20)
reg.grid(row=6, column=1, pady=20)
#------------------------------------------------------------------------------------------

Label(Login,text="Login",font=("Times", "24", "bold")).grid(row=1, column=0, pady=5)
logtext =Entry(Login, width = 30)
logtext.grid(row=2, columns=10, pady=5)

Label(Login,text="MOT de Pass",font=("Times", "14", "bold")).grid(row=3, column=0, pady=5)
passtext =Entry(Login,show="*", width = 30)
passtext.grid(row=4, columns=10, pady=5)
b6 = Button(Login,text="OK",font=("Times", "14", "bold"),width=30,command=connect).grid(row=5, column=0, pady=5)
#--------------------------------------------------------------------------------------------

w.mainloop()
