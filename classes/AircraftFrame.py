import tkinter as tk
from tkinter import messagebox as m_box
import bcrypt
from tkinter import ttk
import mysql.connector
from classes.PlaceholderEntry import PlaceholderEntry
from utils import dbUser, dbPassword, dbHost, dbName


class AircraftFrame(tk.Frame):

    def __init__(self, parent, controller,master=None):
        self.root = master
        super().__init__(master, borderwidth=0, relief=tk.RAISED)

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add an aircraft", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        aircraftInput = PlaceholderEntry(self, placeholder="Aircraft ID")
        weightInput = PlaceholderEntry(self, placeholder="Weight (kg)")
        armInput = PlaceholderEntry(self, placeholder="Arm (m)")

        aircraftInput.pack()
        weightInput.pack()
        armInput.pack()

        button = tk.Button(self, text="Add",
                           command=lambda: self.addAircraft(aircraftInput, weightInput, armInput))

        deleteButton = tk.Button(self, text="Delete",
                           command=lambda: self.deleteAircraft())

        button.pack()
        deleteButton.pack()

        # DB Connection
        database = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword, database=dbName)
        mycursor = database.cursor()
        # Retrieve all values from table Aircraft
        mycursor.execute("SELECT * FROM Aircraft")
        allAirCrafts = mycursor.fetchall()
        database.close()

        columns = ('Aircraft_ID', 'Weight', 'Arm')

        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('Aircraft_ID', text='Aircraft')
        self.tree.heading('Weight', text='Weight (kg)')
        self.tree.heading('Arm', text='Arm (m)')

        # generate sample data
        aircrafts = []
        for n in range(1, len(allAirCrafts)):
            aircrafts.append((f'{allAirCrafts[n][0]}', f'{allAirCrafts[n][1]}', f'{allAirCrafts[n][2]}'))

        # add data to the treeview
        for aircraft in aircrafts:
            self.tree.insert('', tk.END, values=aircraft)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.pack()

        homeButton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame('MainPageFrame'))
        homeButton.pack()

    def deleteAircraft(self):
        self.selected = self.tree.focus()
        values = self.tree.item(self.selected, 'values')
        # DB Connection
        database = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword, database=dbName)
        mycursor = database.cursor()
        # Delete aircraft from DB
        sql = "DELETE FROM Aircraft WHERE Aircraft_ID=%s"
        val = (values[0],)
        mycursor.execute(sql, val)
        database.commit()
        database.close()
        # Delete aircraft from treeview
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)


    def addAircraft(self, aircraft, weight, arm):
        #Ckeck if there is an empty Entry
        if not len(aircraft.get()) or not len(weight.get()) or not len(arm.get()):
            m_box.showerror('Error', 'All fields are required')
            return False

        #Check type of Weight and Arm values
        try:
            int(weight.get())
            int(arm.get())
        except:
            m_box.showerror('Error', 'Only numbers are accepted!')
            return False

        # DB Connection
        database = mysql.connector.connect(host=dbHost, user=dbUser, passwd=dbPassword, database=dbName)
        mycursor = database.cursor()
        #Insert values to DB
        sql = "INSERT INTO Aircraft (Aircraft_ID, Weight, Arm) VALUES (%s, %s, %s)"
        val = (aircraft.get(), weight.get(), arm.get(),)
        mycursor.execute(sql, val)
        database.commit()
        #Insert value to treeview
        aircrafts = (aircraft.get(), weight.get(), arm.get())
        self.tree.insert('', tk.END, values=aircrafts)

        #Clear all enties values
        aircraft.delete(0, 'end')
        weight.delete(0, 'end')
        arm.delete(0, 'end')







