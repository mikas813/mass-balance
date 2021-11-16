import tkinter as tk
from tkinter import messagebox as m_box
import bcrypt
from tkinter import ttk
import mysql.connector
from classes.PlaceholderEntry import PlaceholderEntry


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
        button.pack()


    def addAircraft(self, aircraft, weight, arm):
        #DB Connection
        database = mysql.connector.connect(host='localhost', user='root', passwd='', database='MassAndBalance')
        mycursor = database.cursor()

        #Ckeck if there is an empty Entry
        if not len(aircraft.get()) or not len(weight.get()) or not len(arm.get()):
            m_box.showerror('Error', 'All field are required')
            return False

        #Check type of Weight and Arm values
        try:
            int(weight.get())
            int(arm.get())
        except:
            m_box.showerror('Error', 'Only numbers are accepted!')
            return False


        #Insert values to DB
        sql = "INSERT INTO Aircraft (Aircraft_ID, Weight, Arm) VALUES (%s, %s, %s)"
        val = (aircraft.get(), weight.get(), arm.get(),)
        mycursor.execute(sql, val)
        database.commit()

        #Clear all enties values
        aircraft.delete(0, 'end')
        weight.delete(0, 'end')
        arm.delete(0, 'end')
        self.getAllAircraftsAndDisplay()


    def getAllAircraftsAndDisplay(self):
        # DB Connection
        database = mysql.connector.connect(host='localhost', user='root', passwd='', database='MassAndBalance')
        mycursor = database.cursor()

        # Retrieve all values from table Aircraft
        mycursor.execute("SELECT * FROM Aircraft")
        allAirCrafts = mycursor.fetchall()

        columns = ('Aircraft_ID', 'Weight', 'Arm')

        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('Aircraft_ID', text='Aircraft')
        tree.heading('Weight', text='Weight (kg)')
        tree.heading('Arm', text='Arm (m)')

        # generate sample data
        aircrafts = []
        for n in range(1, len(allAirCrafts)):
            aircrafts.append((f'{allAirCrafts[n][0]}', f'{allAirCrafts[n][1]}', f'{allAirCrafts[n][2]}'))

        # add data to the treeview
        for aircraft in aircrafts:
            tree.insert('', tk.END, values=aircraft)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        tree.pack()

AircraftFrame.getAllAircraftsAndDisplay()



