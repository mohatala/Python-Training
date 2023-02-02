import tkinter as tk
from tkinter import *
import sqlite3
from tkinter.messagebox import *
from tkinter import ttk

conn=sqlite3.connect("C:/Users/21260/Desktop/Master/Python/Controle G article/Garticle.db")
c=conn.cursor()

sql2="""CREATE TABLE IF NOT EXISTS Article(
                            code INTERGER PRIMARY KEY,
                            design TEXT NOT NULL,
                            categorie TEXT NOT NULL,
                            pu DOUBLE NOT NULL,
                            en_solde INTERGER NOT NULL
                            )
     """
c.execute(sql2)
conn.commit()


def insertarticle():
    c=conn.cursor()
    c.execute("INSERT INTO Article VALUES ("+str(txtcode.get())+",'"+txtdesign.get()+"','"+txtcat.get()+"','"+str(txtpu.get())+"',"+str(var1.get())+")")
    conn.commit()
    l=[txtcode.get(),txtdesign.get(),txtcat.get()]
    tree.insert('', tk.END, values=l)
    showinfo("message","Insert succesfuly")

def Deletearticle():
    c=conn.cursor()
    record=0
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values'][0]
    c.execute("DELETE FROM Article WHERE code="+str(record)+"")
    conn.commit()
    for row in tree.get_children():
        tree.delete(row)
    l=selectall()
    l1=[]
    for art in l:
        l1.append(art[:3])

    for c in l1:
        tree.insert('', tk.END, values=c)
    showinfo("message","Deleted succesfuly")

def selectall():
    c=conn.cursor()

    l=[]
    query = "SELECT * FROM Article"
    c.execute(query)
    result = c.fetchall()
    l=result
    return l

#############################################
w = Tk()
w.title("GArticle")
w.geometry("900x500")
##########################

############## Gestion Article########################
framearticle = Frame(w, padx=40, pady=40)

lbl1=Label(framearticle,text="Code Article",font=("Times", "14")).grid(row=1, column=0, pady=2)
txtcode=Entry(framearticle)
txtcode.grid(row=1, column=2, pady=1)

btn1=Button(framearticle,text="Nouveau",command=insertarticle).grid(row=1, column=4, pady=1)

lbl2=Label(framearticle,text="Designation",font=("Times", "14")).grid(row=2, column=0, pady=2)
txtdesign=Entry(framearticle)
txtdesign.grid(row=2, column=2, pady=1)

btn2=Button(framearticle,text="Supprimer",command=Deletearticle).grid(row=2, column=4, pady=1)

lbl3=Label(framearticle,text="Categorie",font=("Times", "14")).grid(row=4, column=0, pady=2)
txtcat = tk.StringVar()
cat = ttk.Combobox(framearticle, textvariable=txtcat)
l=["Informatique","Vetement","Jeux"]
cat['values'] =l
cat['state'] = 'readonly'
cat.grid(row=4, column=2, pady=1)
btn3=Button(framearticle,text="Fermer",command=w.quit).grid(row=4, column=4, pady=1)

lbl4=Label(framearticle,text="Prix unitaire",font=("Times", "14")).grid(row=5, column=0, pady=2)
txtpu=Entry(framearticle)
txtpu.grid(row=5, column=2, pady=1)

var1 = tk.IntVar()
c1 = tk.Checkbutton(framearticle, text='Article en solde',variable=var1, onvalue=1, offvalue=0)
c1.grid(row=6, column=2, pady=1)

columns = ('Code', 'Designation', 'Categorie')

tree = ttk.Treeview(framearticle, columns=columns, show='headings')
tree.heading('Code', text='Code')
tree.heading('Designation', text='Designation')
tree.heading('Categorie', text='Categorie')

l=selectall()
l1=[]
for art in l:
    l1.append(art[:3])

for c in l1:
    tree.insert('', tk.END, values=c)
    


tree.grid(row=8, column=2, pady=2)

framearticle.pack(expand=True)
w.mainloop()
