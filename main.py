import tkinter as tk
from tkinter import messagebox,ttk
from tkinter import simpledialog
from datetime import datetime
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

    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    if os.path.exists(f"{username}pass.txt"):
        with open(f"{username}pass.txt", "r") as pass_file:
            password = pass_file.read().strip()
    else:
        messagebox.showerror("Error", f"Journal for '{username}' hasn't been created")
        return

    password_entry = simpledialog.askstring("Password", f"Enter password for {username}:")

    if password_entry != password:
        messagebox.showerror("Error", "Incorrect password")
        return

    file_path = f"{username}.txt"

    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"Journal for '{username}' hasn't been created")
        return

    read_window = tk.Toplevel(root)
    read_window.title(f"{username}'s Journal")

    canvas = tk.Canvas(read_window)
    scrollbar = ttk.Scrollbar(read_window, orient="vertical", command=canvas.yview)
    frame = ttk.Frame(canvas)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")


    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    line_number = 1

    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                labeled_line = f"{line_number}: ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {line.strip()}"

                message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
                label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
                label.pack(anchor="w", padx=10, pady=5)
                message_frame.pack(fill="x", padx=5, pady=5)
                line_number += 1


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

