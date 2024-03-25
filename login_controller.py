import tkinter as tk
from tkinter import messagebox, simpledialog
from login_model import Model
from login_view import View
from journal_controller import Jcontroller

class Login_Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root)
        self.root = root
        self.view.set_controller(self)
    
    def checkinfo(self, username):
       
        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
    
        entries = self.model.read_entries()
        new_user = 1
        for i, entry in enumerate(entries):
                if entry.strip():
                        userlogin = entry.split()[0]
                        passlogin = entry.split()[1]

                        if username == userlogin :
                            new_user = 0
                            password_entry = simpledialog.askstring("Password", f"Enter password for {username}:")
                            if not password_entry:
                                messagebox.showerror("Error", "Please enter a Password")
                                return 

                            if password_entry != passlogin:
                                messagebox.showerror("Error", "Incorrect password")
                                return
                            else :
                                new_window = tk.Toplevel(self.root)
                                newwindow = Jcontroller(new_window,username)
                            break

        if(new_user) :

            password = simpledialog.askstring("Password", f"Set password for {username}:")
            if not password:
                messagebox.showerror("Error", "Password cannot be empty")
                return
            self.model.new_user(username,password)
            new_window = tk.Toplevel(self.root)
            newwindow = Jcontroller(new_window,username)

def main():
    root = tk.Tk()
    App = Login_Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
