import tkinter as tk
from tkinter import messagebox as m_box
import bcrypt
import mysql.connector
from utils import dbUser, dbPassword, dbHost, dbName
from classes.PlaceholderEntry import PlaceholderEntry


class RegisterFrame(tk.Frame):

    def __init__(self, parent, controller,master=None):
        self.root = master
        super().__init__(master, borderwidth=0, relief=tk.RAISED)

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Register to use Mass&Balance calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        nameInput = PlaceholderEntry(self, placeholder="Username")
        pass1Input = PlaceholderEntry(self, placeholder="Password", show='*')
        pass2Input = PlaceholderEntry(self, placeholder="Confirm password", show='*')

        nameInput.pack()
        pass1Input.pack()
        pass2Input.pack()

        button = tk.Button(self, text="Register",
                           command=lambda: self.register(nameInput, pass1Input, pass2Input))
        button.pack()

        loginButton = tk.Button(self, text="Login",
                           command=lambda: self.controller.show_frame('LoginFrame'))
        loginButton.pack()

    def register(self, username, pass1, pass2):
        database = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword, database=dbName)
        mycursor = database.cursor()

        Username = username.get()
        Password = pass1.get()
        Password1 = pass2.get()

        sql = "SELECT username FROM Users WHERE username = %s"
        val = (Username,)

        mycursor.execute(sql, val)
        checkUsername = mycursor.fetchall()

        if not len(Username):
            m_box.showerror('Error', 'Please enter a username')
            return False

        if Password != Password1:
            m_box.showerror('title', 'Passwords don\'t match!')

        else:
            if len(Password) < 6:
                m_box.showerror('Error', 'Password too short!')
            elif  checkUsername:
                m_box.showerror('Alert', 'User exists!')
            else:
                if Password == Password1:
                    Password = Password.encode('utf-8')
                    Password = bcrypt.hashpw(Password, bcrypt.gensalt())
                    slicedPassword = str(Password)[1:]

                    sql = "INSERT INTO Users (username, password) VALUES (%s, %s)"
                    val = (Username, slicedPassword)
                    mycursor.execute(sql, val)
                    database.commit()

                self.controller.show_frame("LoginFrame")
                m_box.showinfo('Success', 'Success')