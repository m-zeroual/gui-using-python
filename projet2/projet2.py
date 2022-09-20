from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel
from tkinter import messagebox




def Login():
    if (user_text.get() == "admin" and password_text.get() == "admin"):
        messagebox.showinfo("Message info", "login success.")
    else:
        messagebox.showerror("Message d'erreur", "Login or password incorrect")

            

def Add():
    Liste = []
    resulta = (text_nom.get(),
               text_prenom.get(),
               text_combo.get()
               )
    Liste.append(resulta)
    print(resulta)


def Sing_up():
    f = Tk()
    f.geometry("500x400")
   

    nom = Label(f, text="Nom :")
    nom.place (x=20 ,y=20 )

    text_nom=Entry(f)
    text_nom.place(x=100, y=20)

    prenom = Label(f, text="Prenom :")
    prenom.place (x=20 ,y=60)

    text_prenom=Entry(f)
    text_prenom.place(x=100 , y=60)

    
    activite = Label(f, text="activite :")
    activite.place(x=20, y=100)

    n=IntVar()
    text_combo =ttk.Combobox(f , value=["Mr","Mme","Mlle"] )
    text_combo.place(x=100 ,y=100)

    username = Label(f, text="Username :")
    username.place(x=20 , y=140)

    text_username = Entry(f)
    text_username.place(x=100 , y=140)

    password = Label(f, text="Possword :")
    password.place(x=20 , y=180)

    text_password = Entry(f)
    text_password.place(x=100 , y=180)   

    Sing_up = Button(f ,text="Sing up")
    Sing_up.place(x=130 , y=220 ,height=27 ,width=100)

    f.mainloop()
 

def Quitter():
    message=askokcancel("Quit","Do you want to leave ?")
    if message== True:
        f.destroy()

f = Tk()

f.geometry("500x400")

user = Label(f, text="Username :")
user.place(x=200 , y=30)

user_text=Entry(f)
user_text.place(x=160 , y=55)

password = Label(f, text="Password :")
password.place(x=200 , y=110)

password_text=Entry(f)
password_text.place(x=160 , y=135)

Login=Button(f ,text="Login", command = Login)
Login.place(x=190 , y=180 ,height=27 ,width=100)


Quitter = Button(f,text="Quitter" , command = Quitter)
Quitter.place(x=115,y=230 ,height=27 ,width=100)

Sing_up = Button(f ,text="Sing up" ,command = Sing_up)
Sing_up.place(x=250 , y=230 ,height=27 ,width=100)

f.mainloop()
