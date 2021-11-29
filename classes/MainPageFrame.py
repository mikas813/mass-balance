import tkinter as tk
from classes.PlaceholderEntry import PlaceholderEntry
from tkinter import ttk
import mysql.connector

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
        usableFuelInput = PlaceholderEntry(self, placeholder="Usable Fuel (F (l)*ρf(0.72) [kg]")

        pilotInput.grid(row=2, column=1, sticky='W')
        coPilotInput.grid(row=3, column=1, sticky='W')
        baggageInput.grid(row=4, column=1, sticky='W')
        usableFuelInput.grid(row=5, column=1, sticky='W')

        # Second st row's entries
        armLabel = tk.Label(self, text="Arm (m)", font=controller.title_font)
        armLabel.grid(row=1, column=2, pady=20, sticky='W')

        pilotArmInput = PlaceholderEntry(self, placeholder="Pilot m")
        coPilotArmInput = PlaceholderEntry(self, placeholder="Co-Pilot m")
        baggageArmInput = PlaceholderEntry(self, placeholder="Baggage m")
        fuelInputInput = PlaceholderEntry(self, placeholder="???")

        pilotArmInput.grid(row=2, column=2, sticky='W')
        coPilotArmInput.grid(row=3, column=2, sticky='W')
        baggageArmInput.grid(row=4, column=2, sticky='W')
        fuelInputInput.grid(row=5, column=2, sticky='W')

        #Action buttons
        actionBtnsLabel = tk.Label(self, text="Action buttons", font=controller.title_font)
        actionBtnsLabel.grid(row=1, column=3, pady=20, sticky='W')

        calcButton = tk.Button(self, text="Calculate")

        addAirCraftButton = tk.Button(self, text="Add Aircraft",
                           command=lambda: controller.show_frame("AircraftFrame"))
        #Action buttons
        calcButton.grid(row=4, column=3, sticky='W')
        addAirCraftButton.grid(row=5, column=3, sticky='W')
        # DB Connection
        database = mysql.connector.connect(host='localhost', user='root', passwd='', database='MassAndBalance')
        mycursor = database.cursor()
        # Retrieve all values from table Aircraft
        mycursor.execute("SELECT Aircraft_ID FROM Aircraft")
        allAirCrafts = mycursor.fetchall()
        database.close()
        #Combobox
        comboExample = ttk.Combobox(self, values=allAirCrafts)
        comboExample.grid(row=3, column=3, sticky='W')


        #Treeview table
        columns = ('', '', '', '')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        s = ttk.Style()
        s.configure('Treeview', rowheight=2)
        # define headings

        aircrafts = []
        aircrafts.append(('Take-off Condition', '518,3', '1,715', '889,1'))


        # add data to the treeview
        for aircraft in aircrafts:
            self.tree.insert('', tk.END, values=aircraft)

        # add a scrollbar
        self.tree.grid(row=7, columnspan=4, pady=40, sticky='WE')

