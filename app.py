import tkinter as tk 
from tkinter import *

from register import register 
from login import login

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
regButton = Button(signupFrame, text='Register', command =lambda: register(
    '', regUsernameInput, regPasswordInput, regPasswordInput1))
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
regButton = Button(loginFrame, text='Login', command=lambda: login('',
                                                        UsernameInput,
                                                        PasswordInput, 
                                                        homeFrame, 
                                                        loginFrame))
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
