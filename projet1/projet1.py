from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel


def Display():
    newF = Tk()
    newF.geometry("600x150")
    name = enternom.get()
    lname = enterprenom.get()
    if x.get()==1:
        sexe="Malle"
    elif(x.get() == 2) :
        sexe="Femme"
    else:
        sexe=""
    age = list.get()
    if z.get()==1:
        lang="Arabic"
    else :
        lang=""
    if c.get()==1:
        lang1="French"
    else:
        lang1=""
    if a.get()==1:
        lang2="English"
    else :
        lang2 =""
    
    afichlbl = Label(newF , text = "")
    afichlbl.place(x = 50 , y = 50)
    afichlbl["text"]= "Hello " + name + " "  + lname+ " your age is " + age+ " you speake "+lang+" "+lang1+" "+lang2+" your sexe is " +sexe

            

def Reset():
    enternom.delete(0, END)
    enterprenom.delete(0, END)
    list.delete(0, END)
    x.set(0)
    z.set(0)
    c.set(0)
    a.set(0)
def Quit():
    message=askokcancel("Quit","Do you want to leave ?")
    if message== True:
        descp.destroy()
    
descp=Tk()
descp.geometry("400x500")

cadre=LabelFrame(descp, text='Information')
cadre.place(width=300, height=400, x=50, y=20 )

nom=Label(cadre, text="Last Name: ")
nom.grid(row=0, column=0, pady=10)
enternom=Entry(cadre)
enternom.grid(row=0, column=1, pady=10)

prenom=Label(cadre, text="First Name: ")
prenom.grid(row=1, column=0, pady=10)
enterprenom=Entry(cadre)
enterprenom.grid(row=1, column=1, pady=10)

lablist=Label(cadre, text="Age:")
lablist.grid(row=2, column=0, pady=10)

val=[]
for i in range(1,41):
    val.append(str(i))
list=ttk.Combobox(cadre, values=val)
list.grid(row=2, column=1)


Sexe=Label(cadre, text='Sexe:')
Sexe.grid(row=3, column=0)

x=IntVar()
check1=Radiobutton(cadre, text="M",value=1, variable=x)
check2=Radiobutton(cadre,text="F", value=2, variable=x)
check1.place(x=70, y=133)
check2.place(x=150, y=133)

lang=LabelFrame(cadre, text='Languages')
lang.place(x=20, y=170, width=100, height=130)


z=IntVar()
box1=Checkbutton(lang, text="Arabic", variable=z)
box1.place(x=10, y=10)
c=IntVar()
box2=Checkbutton(lang,text="French",variable=c)
box2.place(x=10, y=30)
a=IntVar()
box3=Checkbutton(lang,text="English", variable=a)
box3.place(x=10, y=50)

affichebtn=Button(cadre, text='Display', command=Display)
affichebtn.place(x=20 , y=320, width=100 )

resetbtn=Button(cadre, text='Effacer', command=Reset)
resetbtn.place(x=140 , y=320, width=100 )

quitbtn=Button(descp, text='Quitter', command=Quit)
quitbtn.place(x=150 , y=450, width=100 )



descp.mainloop()
