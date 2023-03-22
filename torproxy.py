from tkinter import *
from tkinter import messagebox
import os
import tkinter as tk
from tkinter import ttk
tk=Tk()
tk.title("proxychains-gui")
tk.geometry("300x70")
def proxy():
    uygulama=e1.get()
    os.system("sudo apt-get install -y proxychains")
    os.system("sudo mv proxychains4.conf /etc/proxychains4.conf")
    os.system("sudo apt-get install -y tor")
    os.system("service tor start")
    os.system("exit")
    os.system("proxychains {}".format(uygulama))

def dur():
    os.system("service tor stop")
l2=Label(tk,text="proxy olacak uygulama (varsayılan = firefox)")
l2.place(x=0,y=10)

e1=Entry(tk,width=20)
e1.insert(0,"firefox")
e1.place(x=1,y=35)

b1=Button(tk, text="Bağlan",command=proxy)
b1.place(x=170,y=30)
b2=Button(tk, text="Dur",command=dur)
b2.place(x=245,y=30)

tk.mainloop()