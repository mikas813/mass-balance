import tkinter as tk
from tkinter import messagebox as m_box
import bcrypt
from classes.PlaceholderEntry import PlaceholderEntry
import mysql.connector


class LoginFrame(tk.Frame):

    def login(self, username, password):
        database = mysql.connector.connect(host='localhost', user='root', passwd='', database='MassAndBalance')
        mycursor = database.cursor()

        Username = username.get()
        Password = password.get()

        sql = "SELECT username, password FROM Users WHERE username=%s"
        val = (Username,)

        mycursor.execute(sql, val)
        usernameAndPassword = mycursor.fetchone()

        if not len(Username or Password) < 1:

                if usernameAndPassword[0] == Username:
                    hashed = usernameAndPassword[1]
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')

                    if bcrypt.checkpw(Password.encode(), hashed):
                        self.controller.show_frame("MainPageFrame")
                    else:
                        m_box.showerror('Error', 'Incorrect Password or Username')
                else:
                    m_box.showerror('Error', 'Username doesn\'t exist')


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller


        label = tk.Label(self, text="Login to Mass&Balance Calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        nameInput = PlaceholderEntry(self, placeholder="Username")
        passInput = PlaceholderEntry(self, placeholder="Password")

        nameInput.pack()
        passInput.pack()

        loginButton = tk.Button(self, text="Login",
                            command=lambda: self.login(nameInput, passInput))

        registerButton = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("RegisterFrame"))
        loginButton.pack()
        registerButton.pack()
