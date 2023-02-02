from tkinter import *



def F1_F2():
    F2.pack(expand=True)
    F1.pack_forget()


def F2_F1():
    F1.pack(expand=True)
    F2.pack_forget()


    
w = Tk()
w.title("DEMO")
w.geometry('500x400')
w.config(bg="#447c84")
w.attributes('-fullscreen',True)


F1 = Frame(w, padx=20, pady=20)
F2 = Frame(w, padx=20, pady=20)


Label(F1,text="In F1").grid(row=1, column=0, pady=5)


Label(F2,text="In F2").grid(row=1, column=0, pady=5)

b1 = Button(w,text="F1->F2",command=F1_F2)
b1.place(x=10,y=10)

b2 = Button(w,text="F2->F1",command=F2_F1)
b2.place(x=700,y=10)
w.mainloop()

