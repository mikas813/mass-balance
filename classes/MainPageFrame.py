import tkinter as tk
from classes.PlaceholderEntry import PlaceholderEntry
from tkinter import ttk
import mysql.connector

class MainPageFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Loading", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        pilotInput = PlaceholderEntry(self, placeholder="Pilot")
        coPilotInput = PlaceholderEntry(self, placeholder="Co-Pilot")
        baggageInput = PlaceholderEntry(self, placeholder="Baggage")
        usableFuelInput = PlaceholderEntry(self, placeholder="Usable Fuel (F (l)*ρf(0.72) [kg]")

        pilotInput.pack()
        coPilotInput.pack()
        baggageInput.pack()
        usableFuelInput.pack()

        calcButton = tk.Button(self, text="Calculate")

        addAirCraftButton = tk.Button(self, text="Add Aircraft",
                           command=lambda: controller.show_frame("AircraftFrame"))

        # DB Connection
        database = mysql.connector.connect(host='localhost', user='root', passwd='', database='MassAndBalance')
        mycursor = database.cursor()
        # Retrieve all values from table Aircraft
        mycursor.execute("SELECT Aircraft_ID FROM Aircraft")
        allAirCrafts = mycursor.fetchall()
        database.close()

        comboExample = ttk.Combobox(self, values=allAirCrafts)
        comboExample.pack()

        calcButton.pack()
        addAirCraftButton.pack()


        #Treeview table
        columns = ('', 'Take-off conditions', '', '')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        s = ttk.Style()
        s.configure('Treeview', rowheight=2)
        # define headings
        self.tree.heading('Take-off conditions', text='Take-off conditions')

        aircrafts = []
        aircrafts.append(('Take-off Condition', '518,3', '1,715', '889,1'))


        # add data to the treeview
        for aircraft in aircrafts:
            self.tree.insert('', tk.END, values=aircraft)

        # add a scrollbar
        self.tree.pack()

