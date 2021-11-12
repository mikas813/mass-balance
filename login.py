from tkinter import messagebox as m_box
import bcrypt
import tkinter as tk
from tkinter import *

def login(self, username, password, homeframe, loginframe):
    print(1)
    db = open('database.txt', 'r')
    Username = username.get()
    Pasword = password.get()

    if not len(Username or Pasword) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(',')
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[Username]:
                hashed = data[Username].strip('b')
                hashed = hashed.replace("'", "")
                hashed = hashed.encode('utf-8')

                try:
                    if bcrypt.checkpw(Pasword.encode(), hashed):
                        homeframe.pack(fill='both', expand=1)
                        loginframe.pack_forget()
                    else:
                        m_box.showerror('Error', 'Wrong password')
                except:
                    m_box.showerror('Error', 'Incorect Password or Username')
            else:
                m_box.showerror('Error', 'Username doesn\'t exists')
        except:
            m_box.showerror('Error', 'Login error')
