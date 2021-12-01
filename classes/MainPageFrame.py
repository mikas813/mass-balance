import tkinter as tk
from classes.PlaceholderEntry import PlaceholderEntry
from tkinter import ttk
import mysql.connector
from tkinter import messagebox as m_box
from utils import dbUser, dbPassword, dbHost, dbName

class MainPageFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #First row's entries
        loadingLabel = tk.Label(self, text="Loading data", font=controller.title_font)
        loadingLabel.grid(row=1, column=1, pady=20, sticky='W')

        pilotInput = PlaceholderEntry(self, placeholder="Pilot")
        coPilotInput = PlaceholderEntry(self, placeholder="Co-Pilot")
        baggageInput = PlaceholderEntry(self, placeholder="Baggage")
        # usableFuelInput = PlaceholderEntry(self, placeholder="Usable Fuel (F (l)*ρf(0.72) [kg]")

        pilotInput.grid(row=2, column=1, sticky='W')
        coPilotInput.grid(row=3, column=1, sticky='W')
        baggageInput.grid(row=4, column=1, sticky='W')
       # usableFuelInput.grid(row=5, column=1, sticky='W')

        # Second st row's entries
        armLabel = tk.Label(self, text="Arm (m)", font=controller.title_font)
        armLabel.grid(row=1, column=2, pady=20, sticky='W')

        pilotArmInput = PlaceholderEntry(self, placeholder="Pilot m")
        coPilotArmInput = PlaceholderEntry(self, placeholder="Co-Pilot m")
        baggageArmInput = PlaceholderEntry(self, placeholder="Baggage m")
        #fuelInputInput = PlaceholderEntry(self, placeholder="???")

        pilotArmInput.grid(row=2, column=2, sticky='W')
        coPilotArmInput.grid(row=3, column=2, sticky='W')
        baggageArmInput.grid(row=4, column=2, sticky='W')
        #fuelInputInput.grid(row=5, column=2, sticky='W')

        #Action buttons
        actionBtnsLabel = tk.Label(self, text="Action buttons", font=controller.title_font)
        actionBtnsLabel.grid(row=1, column=3, pady=20, sticky='W')

        calcButton = tk.Button(self, text="Calculate", command=lambda:  calculate())

        addAirCraftButton = tk.Button(self, text="Add Aircraft",
                           command=lambda: controller.show_frame("AircraftFrame"))
        #Action buttons
        calcButton.grid(row=3, column=3, sticky='W')
        addAirCraftButton.grid(row=4, column=3, sticky='W')

        # DB Connection
        database = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword, database=dbName)
        mycursor = database.cursor()
        # Retrieve all values from table Aircraft
        mycursor.execute("SELECT Aircraft_ID FROM Aircraft")
        allAirCrafts = mycursor.fetchall()
        database.close()
        #Combobox
        comboBox = ttk.Combobox(self, values=allAirCrafts)
        comboBox.grid(row=2, column=3, sticky='W')

        def calculate():
            if not len(pilotInput.get()) or not len(coPilotInput.get()) or not len(baggageInput.get()) \
                    or not len(pilotArmInput.get()) or not len(coPilotArmInput.get()) or not len(baggageArmInput.get()):
                m_box.showerror('Error', 'All fields are required!')
                return  False
            if not len(comboBox.get()):
                m_box.showerror('Error', 'Please select an aircraft!')
                return  False
            print('calc')
            #Get takeoff weight conditions

            # DB Connection
            database = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword, database=dbName)
            mycursor = database.cursor()

            # Get aircraft empty weight by aircraft name
            sql = "SELECT Weight FROM Aircraft WHERE Aircraft_ID=%s"

            #selected aircraft
            val = (comboBox.get(),)
            mycursor.execute(sql, val)
            data = mycursor.fetchall()
            emprtyAircraftWeight = data[0][0]
            database.close()

            pilotWeight = int(pilotInput.get())
            coPilotWeight = int(coPilotInput.get())

            #sum aircraft empty weight + pilot w + co-pilot w
            totalWeight = emprtyAircraftWeight + pilotWeight + coPilotWeight
            print('Take Off conditions ',  totalWeight)
