import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime
import os
import random

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
        write_window.destroy()

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

    def edit_entry(entry_num):
        print("edit functionality")
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Entry")

        
        save_button = tk.Button(edit_window, text="Save Changes", command=save_edit)
        save_button.pack()

    def delete_entry(entry_num):
        
        print("delete functionality")
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Entry")

        confirm_label = tk.Label(delete_window, text="Are you sure you want to delete this entry?")
        confirm_label.pack()

        confirm_button = tk.Button(delete_window, text="Yes", command=confirm_delete)
        confirm_button.pack()

    read_window = tk.Toplevel(root)
    read_window.title(f"{username}'s Journal")

    canvas = tk.Canvas(read_window)
    scrollbar = ttk.Scrollbar(read_window, orient="vertical", command=canvas.yview)
    frame = ttk.Frame(canvas)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    with open(file_path, "r") as file:
        entries = file.readlines()

    for i, entry in enumerate(entries):
        if entry.strip():


            random_number = random.randint(1, 20)
            emojis = [
                "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹",
                "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘",
                "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐",
                "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟",
                "😕", "🙁"
            ]


            entry_num = i + 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            labeled_line = f"{emojis[random_number]} ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {entry.strip()}"

            message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
            label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
            label.pack(anchor="w", padx=10, pady=5)
            message_frame.pack(fill="x", padx=5, pady=5)

            edit_button = tk.Button(message_frame, text="Edit", command=lambda num=entry_num-1: edit_entry(num))
            edit_button.pack(side="left", padx=5)

            delete_button = tk.Button(message_frame, text="Delete", command=lambda num=entry_num-1: delete_entry(num))
            delete_button.pack(side="right", padx=5)

root = tk.Tk()
root.title("Journalify")
root.geometry("1200x700")
root.configure(bg="sky blue")

frame1 = tk.Frame(bg='sky blue')

username_label = tk.Label(frame1, text="Username:", bg='sky blue', fg='#333333', font=("Arial", 16))
username_label.grid(row=0, column=0, padx=20, pady=10, sticky="news")
username_entry = tk.Entry(frame1, font=("Arial", 16))
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

create_button = tk.Button(frame1, text="Write your thoughts...", bg='#00008B', fg='white', font=("Arial", 15), command=create_file)
create_button.grid(row=1, column=0, columnspan=2, pady=5)

read_button = tk.Button(frame1, text="Your Journal", bg='#00008B', fg= 'white', font=("Arial", 15), command=read_file)
read_button.grid(row=2, column=0, columnspan=2, pady=5)

frame1.pack()

root.mainloop()
