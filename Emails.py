import tkinter as tk
from tkinter import *
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from tkinter.filedialog import askopenfile 
from email import encoders
from pathlib import Path
from os.path import basename
import os
import sqlite3

conn =sqlite3.connect("Test.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS  Emails(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   mail TEXT NOT NULL) """)
conn.commit()
def getemails():
    l=[]
    for ligne in c.execute("SELECT mail FROM Emails "):
        l.append(ligne[0])
    for f in l:
        txtlist.insert(END, f + "\n")


files = []
def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Files', '*')])
    fil = os.path.basename(file_path.name)
    files.append(file_path.name)
    print(files)
    if file_path is not None:
        pass 
      
def sendemail():
    msg = MIMEMultipart()
    msg['From'] = txtfrom.get()
    msg['To'] = txtto.get()
    msg['Subject'] = txtobj.get()
    message = txtth.get()
    msg.attach(MIMEText(message))
    for f in files or []:
        with open(f, "rb") as fil: 
            ext = f.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype = ext)
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(f) )
        msg.attach(attachedfile)
    mailserver = smtplib.SMTP('smtp-mail.outlook.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(txtfrom.get(), 'mohammed-064058')
    mailserver.sendmail(txtfrom.get(), txtto.get(), msg.as_string())
    mailserver.quit()
l=[]
def addtolist():
    liste=[(txtto.get())]
    c.execute("INSERT INTO Emails VALUES(null,?)",liste)
    conn.commit()
    txtlist.delete('1.0', END)
    l.append(txtto.get())
    for f in l:
        txtlist.insert(END, f + "\n")

w = Tk()
w.title("Emails")
w.geometry("900x500")
##########################
############## Gestion Emails########################
frame = Frame(w, padx=40, pady=40)
lbl=Label(frame,text="Nouveau Email",font=("Times", "24", "bold")).grid(row=0, column=0, pady=2)
lbl1=Label(frame,text="From",font=("Times", "14")).grid(row=1, column=0, pady=2)
txtfrom=Entry(frame)
txtfrom.grid(row=1, column=2, pady=1)
lbl2=Label(frame,text="To",font=("Times", "14")).grid(row=2, column=0, pady=2)
txtto=Entry(frame)
txtto.grid(row=2, column=2, pady=1)
btn4=Button(frame,text=">>",command=addtolist).grid(row=2, column=4, pady=1)
txtlist=tk.Text(frame, height=10, width=30)
txtlist.grid(row=4, column=5, pady=1)
lbl3=Label(frame,text="Object",font=("Times", "14")).grid(row=4, column=0, pady=2)
txtobj=Entry(frame)
txtobj.grid(row=4, column=2, pady=1)
lbl4=Label(frame,text="Theme",font=("Times", "14")).grid(row=8, column=0, pady=2)
txtth=Entry(frame)
txtth.grid(row=8, column=2, pady=1)
lbl5=Label(frame,text="Fichier...",font=("Times", "14")).grid(row=9, column=0, pady=2)
msbtn = Button(frame, text ='Parcourir', command = lambda:open_file()) 
msbtn.grid(row=10, column=1)
envoyer=Button(frame,text="Envoyer",width=20,command=sendemail).grid(row=11, column=1, pady=1)
frame.pack(expand=True)
getemails()

w.mainloop()