import tkinter as tk

class MainPageFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Mass&Balance Calculator", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Add Aircraft",
                           command=lambda: controller.show_frame("AircraftFrame"))
        button.pack()
