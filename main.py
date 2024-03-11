import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime
import os
import random

def save_password(username, password):
    with open(f"{username}pass.txt", "w") as pass_file:
        pass_file.write(password)


def checkinfo() :
    print("to check username and pass")
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
    else :
        nexwin()

def create_file():
    username = username_entry.get()
   
   
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
    file_path = f"{username}.txt"

    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"Journal for '{username}' hasn't been created")
        return

    def edit_entry(entry_num):
        read_window.destroy()
        def save_edit():
            edited_content = entry_content.get("1.0", tk.END)
            with open(file_path, "r") as file:
                lines = file.readlines()
            lines[entry_num] = edited_content
            with open(file_path, "w") as file:
                file.writelines(lines)
            messagebox.showinfo("Success", "Entry edited successfully")
            edit_window.destroy()
            read_file()

        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Entry")

        with open(file_path, "r") as file:
            lines = file.readlines()
        original_content = lines[entry_num]

        entry_content = tk.Text(edit_window)
        entry_content.insert(tk.END, original_content)
        entry_content.pack(fill="both", expand=True)

        save_button = tk.Button(edit_window, text="Save Changes", command=save_edit)
        save_button.pack()

    def delete_entry(entry_num):
        read_window.destroy()
        def confirm_delete():
            with open(file_path, "r") as file:
                lines = file.readlines()
            del lines[entry_num]
            with open(file_path, "w") as file:
                file.writelines(lines)
            messagebox.showinfo("Success", "Entry deleted successfully")
            delete_window.destroy()
            read_file()

        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Entry")

        confirm_label = tk.Label(delete_window, text="Are you sure you want to delete this entry?")
        confirm_label.pack()

        confirm_button = tk.Button(delete_window, text="Yes", command=confirm_delete)
        confirm_button.pack()


    

    def filter_entries():
      
        selected_filter = filter_combobox.get()

        if selected_filter == "Ascending Order":
            sort_key = lambda entry: entry["text"]
            reverse = False
        elif selected_filter == "Descending Order":
            sort_key = lambda entry: entry["text"]
            reverse = True
        else:
            messagebox.showerror("Error", "Please select a valid filter option")
            return

        for widget in frame.winfo_children():
            widget.destroy()

        with open(file_path, "r") as file:
            entries = file.readlines()

        if reverse:
            entries.reverse()

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
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                labeled_line = f"{emojis[random_number]} ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {entry.strip()}"

                message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
                label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
                label.pack(anchor="w", padx=10, pady=5)
                message_frame.pack(fill="x", padx=5, pady=5)

                edit_button = tk.Button(message_frame, text="Edit", command=lambda num=i: edit_entry(num))
                edit_button.pack(side="left", padx=5)

                delete_button = tk.Button(message_frame, text="Delete", command=lambda num=i: delete_entry(num))
                delete_button.pack(side="right", padx=5)



    def search_entries():
        keyword = search_entry.get().strip().lower()

        if not keyword:
            messagebox.showerror("Error", "Please enter a search keyword")
            return

        for widget in frame.winfo_children():
            widget.destroy()

        with open(file_path, "r") as file:
            entries = file.readlines()

        for i, entry in enumerate(entries):
            if entry.strip().lower().find(keyword) != -1:
                random_number = random.randint(1, 20)
                emojis = [
                    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹",
                    "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘",
                    "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐",
                    "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟",
                    "😕", "🙁"
                ]
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                labeled_line = f"{emojis[random_number]} ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {entry.strip()}"

                message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
                label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
                label.pack(anchor="w", padx=10, pady=5)
                message_frame.pack(fill="x", padx=5, pady=5)

                edit_button = tk.Button(message_frame, text="Edit", command=lambda num=i: edit_entry(num))
                edit_button.pack(side="left", padx=5)

                delete_button = tk.Button(message_frame, text="Delete", command=lambda num=i: delete_entry(num))
                delete_button.pack(side="right", padx=5)

    read_window = tk.Toplevel(root)
    read_window.title(f"{username}'s Journal")

    search_frame = ttk.Frame(read_window)
    search_frame.pack(fill="x", padx=5, pady=5)

    search_entry = tk.Entry(search_frame)
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(search_frame, text="Search", command=search_entries)
    search_button.pack(side="left", padx=5)

    filter_options = [
            "Ascending Order",
            "Descending Order"
        ]

    filter_combobox = ttk.Combobox(search_frame, values=filter_options, state="Date Ascending")
    filter_combobox.pack(side="left", padx=5)


    filter_button = tk.Button(search_frame, text="Filter", command=filter_entries)
    filter_button.pack(side="left", padx=5)

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
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            labeled_line = f"{emojis[random_number]} ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {entry.strip()}"

            message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
            label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
            label.pack(anchor="w", padx=10, pady=5)
            message_frame.pack(fill="x", padx=5, pady=5)

            edit_button = tk.Button(message_frame, text="Edit", command=lambda num=i: edit_entry(num))
            edit_button.pack(side="left", padx=5)

            delete_button = tk.Button(message_frame, text="Delete", command=lambda num=i: delete_entry(num))
            delete_button.pack(side="right", padx=5)
    


root = tk.Tk()
root.title("Journalify")
root.geometry("1200x700")
root.configure(bg="sky blue")

frame1 = tk.Frame(bg='sky blue')
def nexwin() :
    username = username_entry.get()
    new_window = tk.Toplevel(root)
    new_window.title(f"Journalify : USER({username})")
    new_window.geometry("1200x700")
    new_window.configure(bg="sky blue")

    frame2 = tk.Frame(new_window,bg='sky blue')
    u_label = tk.Label(frame1, text="Username:", bg='sky blue', fg='#333333', font=("Arial", 16))
    u_label.grid(row=0, column=0, padx=20, pady=10, sticky="news")
    create_button = tk.Button(frame2, text="Write your thoughts...", bg='#00008B', fg='white', font=("Arial", 15), command=create_file)
    create_button.grid(row=1, column=0, columnspan=2, pady=5)
    read_button = tk.Button(frame2, text="Your Journal", bg='#00008B', fg= 'white', font=("Arial", 15), command=read_file)
    read_button.grid(row=2, column=0, columnspan=2, pady=5)
    frame2.pack()



username_label = tk.Label(frame1, text="Username:", bg='sky blue', fg='#333333', font=("Arial", 16))
username_label.grid(row=0, column=0, padx=20, pady=10, sticky="news")
username_entry = tk.Entry(frame1, font=("Arial", 16))
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
check_info = tk.Button(frame1, text="...Go...", bg='#00008B', fg='white', font=("Arial", 15), command=checkinfo)
check_info.grid(row=1, column=0, columnspan=2, pady=5)


frame1.pack()

root.mainloop()
