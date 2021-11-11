import tkinter as tk 
from tkinter import *
from tkinter import messagebox as m_box
import bcrypt
import os 
os.system('clear')

# Create an instance of tkinter frame or window
root = tk.Tk()
root.title('Descktop app with python')
# Set the size of the window
root.geometry('400x600')

# Create frames in the window
loginFrame = tk.Frame(root)
signupFrame = tk.Frame(root)
homeFrame = tk.Frame(root)
#Pack default frame
loginFrame.pack()

#Define register frmame
SignupLabel = Label(signupFrame, text='Signup ')
SignupLabel.pack()

Username = Label(signupFrame, text='Enter your name')
Username.pack()
regUsernameInput = Entry(signupFrame, width=30)
regUsernameInput.pack()

Password = Label(signupFrame, text='Enter your password')
Password.pack()
regPasswordInput = Entry(signupFrame, width=30)
regPasswordInput.pack()

Password1 = Label(signupFrame, text='Confirm your password')
Password1.pack()
regPasswordInput1 = Entry(signupFrame, width=30)
regPasswordInput1.pack()

# Register logic
def register():
    db = open('database.txt', 'r')
    Username = regUsernameInput.get()
    Pasword = regPasswordInput.get()
    Pasword1 = regPasswordInput1.get()
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

regButton = Button(signupFrame, text='Register', command=register)
regButton.pack()

#Redirect to login frame function
def goToLogin():
    loginFrame.pack(fill='both', expand=1)
    signupFrame.pack_forget()
#Display to login button
toLoginButton = Button(signupFrame, text='Login', command=goToLogin)
toLoginButton.pack()
#Display the login's frame inputs
LoginLabel = Label(loginFrame, text='Login ')
LoginLabel.pack()

Username = Label(loginFrame, text='Enter your name')
Username.pack()
UsernameInput = Entry(loginFrame, width=30)
UsernameInput.pack()

Password = Label(loginFrame, text='Enter your password')
Password.pack()
PasswordInput = Entry(loginFrame, width=30)
PasswordInput.pack()

#Login function
def access():
    db = open('database.txt', 'r')
    Username = UsernameInput.get()
    Pasword = PasswordInput.get()

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
                        m_box.showinfo('Alert', 'Login success')
                        homeFrame.pack(fill='both', expand=1)
                        loginFrame.pack_forget() 
                    else:
                        m_box.showerror('Error', 'Wrong password')
                except:
                    m_box.showerror('Error', 'Incorect Password or Username')
            else:
                m_box.showerror('Error', 'Username doesn\'t exists')
        except:
            m_box.showerror('Error', 'Login error')

regButton = Button(loginFrame, text='Login', command=access)
regButton.pack()

#Sign off function
def signOff():
    loginFrame.pack(fill='both', expand=1)
    homeFrame.pack_forget()
    
#Switch to login function
def switchToSignIn():
    signupFrame.pack(fill='both', expand=1)
    loginFrame.pack_forget()

#Display signoff button on home frame
signOffButton = Button(homeFrame, text='Sign Off', command=signOff)
signOffButton.pack()

#Display signup button on signin frame
signinButton = Button(loginFrame, text='Register', command=switchToSignIn)
signinButton.pack()

homeMessage = Label(homeFrame, text='Welcome')
homeMessage.pack()

root.mainloop()
