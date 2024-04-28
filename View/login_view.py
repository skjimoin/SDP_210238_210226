import tkinter as tk

class View:
    def __init__(self, master):
        self.master = master
        self.master.title("Journalify Log in")
        self.master.geometry("1000x692")
        self.master.configure(bg="#E6E6FA")


        self.title_label = tk.Label(self.master, text="JOURNALIFY", bg="#E6E6FA", fg="#800080", font=("Verdana", 36, "bold"))
        self.title_label.pack(pady=(20, 0)) 
        self.title_label = tk.Label(self.master, text="'Where every thought finds its place'", bg="#E6E6FA", fg="blue", font=("Verdana", 10, "bold"))
        self.title_label.pack(pady=(0, 20)) 

        self.journal_image = tk.PhotoImage(file="Images/journaling.png")     
        self.journal_image = self.journal_image.subsample(2)    
        self.image_label = tk.Label(self.master, image=self.journal_image, bg="#E6E6FA")
        self.image_label.pack(pady=20)
        self.frame1 = tk.Frame(bg="#E6E6FA")
        self.username_label = tk.Label(self.frame1, text="Username:", bg="#E6E6FA", fg="black", font=("Verdana", 16))
        self.username_label.grid(row=0, column=0, padx=20, pady=10, sticky="news")
        self.username_entry = tk.Entry(self.frame1, font=("Verdana", 16))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.check_info = tk.Button(self.frame1, text="Enter to your Journal...",  bg="white", fg="#800080", font=("Verdana", 15), 
                                     command=self.check_info_from_controller)
        self.check_info.grid(row=1, column=0, columnspan=2, pady=5)
        self.frame1.pack()

    def set_controller(self, controller):
        self.controller = controller

    def check_info_from_controller(self):
        username = self.username_entry.get()
        self.controller.checkinfo(username)

def main():
    root = tk.Tk()
    app = View(root)
    root.mainloop()

if __name__ == "__main__":
    main()
