import tkinter as tk
from tkinter import messagebox as m_box
import bcrypt
from classes.PlaceholderEntry import PlaceholderEntry
import mysql.connector
from utils import dbUser, dbPassword, dbHost, dbName

class LoginFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller


        label = tk.Label(self, text="Login to Mass&Balance Calculator", font=controller.title_font)
        label.grid(row=1, columnspan=2, ipady=20, ipadx=150)

        nameInput = PlaceholderEntry(self, placeholder="Username")
        passInput = PlaceholderEntry(self, placeholder="Password", show="*")

        nameInput.grid(row=2, columnspan=2, padx=150)
        passInput.grid(row=3, columnspan=2, pady=10, padx=150)

        loginButton = tk.Button(self, text="Login",
                            command=lambda: self.login(nameInput, passInput))

        registerButton = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("RegisterFrame"))
        loginButton.grid(row=4, columnspan=2)
        registerButton.grid(row=5, columnspan=2)


    def login(self, username, password):
        database = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword, database=dbName)
        mycursor = database.cursor()

        Username = username.get()
        Password = password.get()

        sql = "SELECT username, password FROM Users WHERE username=%s"
        val = (Username,)

        mycursor.execute(sql, val)
        usernameAndPassword = mycursor.fetchone()

        try:
            hashed = usernameAndPassword[1]
            hashed = hashed.replace("'", "")
            hashed = hashed.encode('utf-8')
            if bcrypt.checkpw(Password.encode(), hashed):
                self.controller.show_frame("MainPageFrame")
            else:
                m_box.showerror('Error', 'Incorrect Password or Username')
        except:
            m_box.showerror('Error', 'Username doesn\'t exist')





