from tkinter import messagebox as m_box
import bcrypt
import tkinter as tk
from tkinter import *

def register(self, username, pass1, pass2):
    print(11)
    db = open('database.txt', 'r')
    Username = username.get()
    Pasword = pass1.get()
    Pasword1 = pass2.get()
    d = []
    f = []
    for i in db:
        a, b = i.split(',')
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if not len(Username):
        m_box.showerror('Error', 'Please enter a username')

    if Pasword != Pasword1:
        m_box.showerror('title', 'Paswords doesn\'t match!')

    else:
        if len(Pasword) <= 6:
            m_box.showerror('Error', 'Password too short!')
        elif Username in d:
            m_box.showerror('User exists!')
        else:
            if Pasword == Pasword1:
                Pasword = Pasword.encode('utf-8')
                Pasword = bcrypt.hashpw(Pasword, bcrypt.gensalt())

            db = open('database.txt', 'a')
            db.write(Username+", "+str(Pasword)+"\n")
            m_box.showinfo('Success', 'Succes')
