import tkinter as tk
import openpyxl
from tkinter import *
from register import register 
from login import login
from tkinter import ttk
import os 
os.system('clear')

# Create an instance of tkinter frame or window
root = tk.Tk()
root.title('Mass & Balance calculator')
# Set the size of the window
root.geometry('800x400')

# Create frames in the window
loginFrame = tk.Frame(root)
signupFrame = tk.Frame(root)
homeFrame = tk.Frame(root)

#Pack default frame
# loginFrame.pack()
homeFrame.pack()

#Define register frmame
# SignupLabel = Label(signupFrame, text='Signup ')
# SignupLabel.pack()
#
# Username = Label(signupFrame, text='Enter your name')
# Username.pack()
# regUsernameInput = Entry(signupFrame, width=30)
# regUsernameInput.pack()
#
# Password = Label(signupFrame, text='Enter your password')
# Password.pack()
# regPasswordInput = Entry(signupFrame, width=30)
# regPasswordInput.pack()
#
# Password1 = Label(signupFrame, text='Confirm your password')
# Password1.pack()
# regPasswordInput1 = Entry(signupFrame, width=30)
# regPasswordInput1.pack()

# Register logic
# regButton = Button(signupFrame, text='Register', command =lambda: register(
#     '', regUsernameInput, regPasswordInput, regPasswordInput1))
# regButton.pack()

#Redirect to login frame function
# def goToLogin():
#     loginFrame.pack(fill='both', expand=1)
#     signupFrame.pack_forget()
#
# #Display to login button
# toLoginButton = Button(signupFrame, text='Login', command=goToLogin)
# toLoginButton.pack()
# #Display the login's frame inputs
# un = StringVar(root, value='mikas')
# LoginLabel = Label(loginFrame, text='Login ', textvariable=un)
# LoginLabel.pack()
#
# Username = Label(loginFrame, text='Enter your name')
# Username.pack()
# UsernameInput = Entry(loginFrame, width=30)
# UsernameInput.pack()
#
# Password = Label(loginFrame, text='Enter your password')
# Password.pack()
# ps = StringVar(root, value='vfveczvf')
# PasswordInput = Entry(loginFrame, width=30, textvariable=ps)
# PasswordInput.pack()
#
# #Login function
# regButton = Button(loginFrame, text='Login', command=lambda: login('',
#                                                         UsernameInput,
#                                                         PasswordInput,
#                                                         homeFrame,
#                                                         loginFrame))
# regButton.pack()

#Sign off function
# def signOff():
#     loginFrame.pack(fill='both', expand=1)
#     homeFrame.pack_forget()
#
# #Switch to login function
# def switchToSignIn():
#     signupFrame.pack(fill='both', expand=1)
#     loginFrame.pack_forget()
#
# #Display signoff button on home frame
# signOffButton = Button(homeFrame, text='Sign Off', command=signOff)
# signOffButton.pack()
#
# #Display signup button on signin frame
# signinButton = Button(loginFrame, text='Register', command=switchToSignIn)
# signinButton.pack()
#
# homeMessage = Label(homeFrame, text='Welcome {Username}')
# homeMessage.pack()

#excel writer logic
pilotLabel = Label(homeFrame, text='Pilot (kg)')
pilotLabel.pack()
pilotInput = Entry(homeFrame, width=10)
pilotInput.pack()

coPilotLabel = Label(homeFrame, text='Co-Pilot (kg)')
coPilotLabel.pack()
coPilotInput = Entry(homeFrame, width=10)
coPilotInput.pack()

baggageLabel = Label(homeFrame, text='Baggage (kg)')
baggageLabel.pack()
baggageInput = Entry(homeFrame, width=10)
baggageInput.pack()

#Update Mass and Balance sheet's values
def addNameToSheet():
        xfile = openpyxl.load_workbook('PFB.xlsx', data_only=True)
        sheet = xfile['Mass and Balance Sheet']
        sheet['B5'] = pilotInput.get()
        sheet['B6'] = coPilotInput.get()
        sheet['B7'] = baggageInput.get()

        xfile.save('PFB.xlsx')
        sheet_ranges = xfile['Mass and Balance Sheet']

        takeOffW = "%.2f" % sheet_ranges['B10'].value
        takeArm = "%.2f" % sheet_ranges['C10'].value
        takeMoment = "%.2f" % sheet_ranges['D10'].value
        landingW = "%.2f" % sheet_ranges['B12'].value
        landingArm = "%.2f" % sheet_ranges['B12'].value
        landingMoment = "%.2f" % sheet_ranges['B12'].value
        fullReqW = "%.2f" % sheet_ranges['B13'].value
        fullReqArm = "%.2f" % sheet_ranges['B13'].value
        fullReqMoment = "%.2f" % sheet_ranges['B13'].value
        Title = Label(homeFrame, height=4, text='Mass & Balance Tecnam P2002')
        Title.pack()

        # Create an object of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(root, column=("", "", "", ""), show='headings', height=3)

        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="W (kg)")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Arm (m)")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Moment (M) = W*Arm [kg*m]")

        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('Take-off Condition',
                                                 takeOffW,
                                                 takeArm,
                                                 takeMoment))
        tree.insert('', 'end', text="1", values=('Fuel Required (Fuel (liters)*ρfuel(0.72) [kg]',
                                                 landingW,
                                                 landingArm,
                                                 landingMoment))
        tree.insert('', 'end', text="1", values=('Landing Condition',
                                                 fullReqW,
                                                 fullReqArm,
                                                 fullReqMoment))

        tree.pack()

addNameButton = Button(homeFrame, text='Calculate', command=addNameToSheet)
addNameButton.pack()



root.mainloop()
