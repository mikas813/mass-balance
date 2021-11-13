import tkinter as tk
from tkinter import messagebox as m_box
import bcrypt

from classes.PlaceholderEntry import PlaceholderEntry


class RegisterFrame(tk.Frame):

    def register(self, username, pass1, pass2):
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

        if not len(Username):
            m_box.showerror('Error', 'Please enter a username')
            return False

        if Pasword != Pasword1:
            m_box.showerror('title', 'Passwords don\'t match!')

        else:
            if len(Pasword) <= 6:
                m_box.showerror('Error', 'Password too short!')
            elif Username in d:
                m_box.showerror('Alert', 'User exists!')
            else:
                if Pasword == Pasword1:
                    Pasword = Pasword.encode('utf-8')
                    Pasword = bcrypt.hashpw(Pasword, bcrypt.gensalt())

                db = open('database.txt', 'a')
                db.write(Username + ", " + str(Pasword) + "\n")
                self.controller.show_frame("LoginFrame")
                m_box.showinfo('Success', 'Success')

    def __init__(self, parent, controller,master=None):
        self.root = master
        super().__init__(master, borderwidth=0, relief=tk.RAISED)

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Register to use Mass&Balance calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        nameInput = PlaceholderEntry(self, placeholder="Username")
        pass1Input = PlaceholderEntry(self, placeholder="Password")
        pass2Input = PlaceholderEntry(self, placeholder="Confirm password")

        nameInput.pack()
        pass1Input.pack()
        pass2Input.pack()

        button = tk.Button(self, text="Register",
                           command=lambda: self.register(nameInput, pass1Input, pass2Input))
        button.pack()