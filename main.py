import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os

def save_password(username, password):
    with open(f"{username}pass.txt", "w") as pass_file:
        pass_file.write(password)

def create_file():
    username = username_entry.get()
   
    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    if os.path.exists(f"{username}pass.txt"):
        with open(f"{username}pass.txt", "r") as pass_file:
            password = pass_file.read().strip()
    else:
        password = simpledialog.askstring("Password", f"Set password for {username}:")

        if not password:
            messagebox.showerror("Error", "Password cannot be empty")
            return

        save_password(username, password)

    password_entry = simpledialog.askstring("Password", f"Enter password for {username}:")

    if password_entry != password:
        messagebox.showerror("Error", "Incorrect password")
        return

    file_path = f"{username}.txt"
    write_window = tk.Toplevel(root)
    write_window.title(f"{username}'s Journal")

    def save_content():
       
        content = text_area.get("1.0", tk.END)
        mode = "w" if not os.path.exists(file_path) else "a"
        with open(file_path, mode) as file:
            if mode == "a":
                file.write("\n")  
            file.write(content)
        messagebox.showinfo("Success", f"{username}'s Journal updated.")

    text_area = tk.Text(write_window)
    text_area.pack(fill="both", expand=True)

    save_button = tk.Button(write_window, text="Update Journal", command=save_content)
    save_button.pack()

def read_file():
    username = username_entry.get()

    print("will read and organize the journal")






root = tk.Tk()
root.title("Journalify")
root.geometry("1200x700")


username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

create_button = tk.Button(root, text="Write your thoughts...", command=create_file)
create_button.grid(row=1, column=0, columnspan=2, pady=5)

read_button = tk.Button(root, text="Your Journal", command=read_file)
read_button.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()

