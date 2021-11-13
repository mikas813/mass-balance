import tkinter as tk

import bcrypt

from classes.PlaceholderEntry import PlaceholderEntry


class LoginFrame(tk.Frame):

    def login(self, username, password, m_box=None):

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
                            self.controller.show_frame("MainPageFrame")
                        else:
                            m_box.showerror('Error', 'Wrong password')
                    except:
                        m_box.showerror('Error', 'Incorrect Password or Username')
                else:
                    m_box.showerror('Error', 'Username doesn\'t exist')
            except:
                m_box.showerror('Error', 'Login error')

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
