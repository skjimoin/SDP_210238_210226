import tkinter as tk
from tkinter import filedialog

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Text File Input")       
        self.master.geometry("1200x700")
        self.master.configure(bg="sky blue")
        self.frame1 = tk.Frame(bg='sky blue')
        
        self.username_label = tk.Label(self.frame1, text="Username:", bg='sky blue', fg='#333333', font=("Arial", 16))
        self.username_label.grid(row=0, column=0, padx=20, pady=10, sticky="news")
        self.username_entry = tk.Entry(self.frame1, font=("Arial", 16))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.check_info = tk.Button(self.frame1, text="...Go...", bg='#00008B', fg='white', font=("Arial", 15), command=self.checkinfoforcontroller)
        self.check_info.grid(row=1, column=0, columnspan=2, pady=5)
        self.frame1.pack()

    def set_controller(self, controller):
        self.controller = controller

    def checkinfoforcontroller(self):
        username = self.username_entry.get()
        self.controller.checkinfo(username)
