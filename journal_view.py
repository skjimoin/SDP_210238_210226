import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import random
class View:
    def __init__(self, master):


        #new window
        self.master = master
        self.master.title("Journalify")
        self.master.geometry("1200x700")
        self.master.configure(bg="sky blue")   
        self.frame2 = tk.Frame(self.master,bg='sky blue')
        self.create_button = tk.Button(self.frame2, text="Write your thoughts...", bg='#00008B', fg='white', font=("Arial", 15), command=self.save_content_in_controller)
        self.create_button.grid(row=1, column=0, columnspan=2, pady=5)
        self.read_button = tk.Button(self.frame2, text="Your Journal", bg='#00008B', fg= 'white', font=("Arial", 15), command=self.read_file_from_controller)
        self.read_button.grid(row=2, column=0, columnspan=2, pady=5)
        self.frame2.pack()

    def set_controller(self, controller):
        self.controller = controller
   
    def save_content_in_controller(self):

        username = self.controller.username
        write_window = tk.Toplevel(self.master)
        write_window.title(f"{username}'s Journal")

        def save_content():
            content = text_area.get("1.0", tk.END)
            self.controller.create_file(content)
            write_window.destroy()

        text_area = tk.Text(write_window)
        text_area.pack(fill="both", expand=True)
        save_button = tk.Button(write_window, text="Update Journal", command=save_content)
        save_button.pack()

    def read_file_from_controller(self):
        username = self.controller.username

        def filter_entries(): 


            def currect_order_func(i,reverse) :
                if reverse :        
                    file_path = 'journal.txt'

                    with open(file_path, 'r') as file:
                        line_count = sum(1 for line in file)
                        line_count -= 1

                    return line_count - i
                else :
                    return i 

            selected_filter = filter_combobox.get()
            if selected_filter == "Ascending Order":
                reverse = False
            elif selected_filter == "Descending Order":
                reverse = True
            else:
                messagebox.showerror("Error", "Please select a valid filter option")
                return

            for widget in frame.winfo_children():
                widget.destroy()

            entries = self.controller.read_file()
            if reverse:
                entries.reverse()

            usernamenotfound = 1
            for i, entry in enumerate(entries):
                if entry.strip() and entry.strip().split()[0] == username :
                    
                    part = entry.split(' ')
                    text = ' '.join(part[1:])
                    usernamenotfound = 0
                    random_number = random.randint(1, 20)
                    emojis = [
                                "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹",
                                "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘",
                                "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐",
                                "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟",
                                "😕", "🙁"
                            ]

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    labeled_line = f"{emojis[random_number]} ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {text.strip()}"

                    message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
                    label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
                    label.pack(anchor="w", padx=10, pady=5)
                    message_frame.pack(fill="x", padx=5, pady=5)
                    currect_order_num = currect_order_func(i,reverse)
                    edit_button = tk.Button(message_frame, text="Edit", command=lambda num=currect_order_num: self.show_edit_window(num,read_window))
                    edit_button.pack(side="left", padx=5)

                    delete_button = tk.Button(message_frame, text="Delete", command=lambda num=currect_order_num : delete_entry(num))
                    delete_button.pack(side="right", padx=5)
                                
            if (usernamenotfound) :
                messagebox.showerror("Error", f"Journal for '{username}' has no entry.")
                return

        def search_entries():
            keyword = search_entry.get().strip().lower()

            if not keyword:
                messagebox.showerror("Error", "Please enter a search keyword")
                return

            for widget in frame.winfo_children():
                widget.destroy()

            entries = self.controller.read_file()
            usernamenotfound = 1
            for i, entry in enumerate(entries):
                if entry.strip() and entry.strip().split()[0] == username and entry.strip().lower().find(keyword) != -1:
                
                    part = entry.split(' ')
                    text = ' '.join(part[1:])
                    usernamenotfound = 0
                    random_number = random.randint(1, 20)
                    emojis = [
                                "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹",
                                "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘",
                                "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐",
                                "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟",
                                "😕", "🙁"
                            ]
         
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    labeled_line = f"{emojis[random_number]} ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {text.strip()}"

                    message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
                    label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
                    label.pack(anchor="w", padx=10, pady=5)
                    message_frame.pack(fill="x", padx=5, pady=5)

                    edit_button = tk.Button(message_frame, text="Edit", command=lambda num=i: self.show_edit_window(num,read_window))
                    edit_button.pack(side="left", padx=5)

                    delete_button = tk.Button(message_frame, text="Delete", command=lambda num=i: delete_entry(num))
                    delete_button.pack(side="right", padx=5)
                    
            if (usernamenotfound) :

                messagebox.showerror("Error", f"Journal for '{username}' has no entry.")
                return

        read_window = tk.Toplevel(self.master)
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
        filter_button = tk.Button(search_frame, text="Filter",command=filter_entries)
        filter_button.pack(side="left", padx=5)

        canvas = tk.Canvas(read_window)
        scrollbar = ttk.Scrollbar(read_window, orient="vertical", command=canvas.yview)
        frame = ttk.Frame(canvas)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        entries = self.controller.read_file()
        usernamenotfound = 1
        for i, entry in enumerate(entries):
            if entry.strip() and entry.strip().split()[0] == username:
            
                part = entry.split(' ')
                text = ' '.join(part[1:])       
                usernamenotfound = 0
                random_number = random.randint(1, 20)
                emojis = [
                            "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲", "🥹",
                            "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘",
                            "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐",
                            "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟",
                            "😕", "🙁"
                        ]

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                labeled_line = f"{emojis[random_number]} ({username})    Date: {timestamp.split()[0]} | Time: {timestamp.split()[1]} \n    >> {text.strip()}"

                message_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
                label = ttk.Label(message_frame, text=labeled_line, wraplength=600, justify="left")
                label.pack(anchor="w", padx=10, pady=5)
                message_frame.pack(fill="x", padx=5, pady=5)

                edit_button = tk.Button(message_frame, text="Edit",command=lambda num=i: self.show_edit_window(num,read_window))
                edit_button.pack(side="left", padx=5)

                delete_button = tk.Button(message_frame, text="Delete", command=lambda num=i: delete_entry(num))
                delete_button.pack(side="right", padx=5)
                        
        
        if (usernamenotfound) :
            messagebox.showerror("Error", f"Journal for '{username}' has no entry.")
            return
        
        def delete_entry(entry_num):
            read_window.destroy()
            def confirm_delete():
                self.controller.delete_entry(entry_num)
                messagebox.showinfo("Success", "Entry deleted successfully")
                delete_window.destroy()
                self.read_file_from_controller()

            delete_window = tk.Toplevel(self.master)
            delete_window.title("Delete Entry")

            confirm_label = tk.Label(delete_window, text="Are you sure you want to delete this entry?")
            confirm_label.pack()

            confirm_button = tk.Button(delete_window, text="Yes", command=confirm_delete)
            confirm_button.pack()
                
    def show_edit_window(self, entry_num,master_window):
        master_window.destroy()
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Entry")

        lines = self.controller.read_file()
        original_content = lines[entry_num]
        part = original_content.split(' ')
        text = ' '.join(part[1:])
        entry_content = tk.Text(edit_window)
        entry_content.insert(tk.END, text)
        entry_content.pack(fill="both", expand=True)

        save_button = tk.Button(edit_window, text="Save Changes", command=lambda: self.controller.save_edit(entry_num, entry_content.get("1.0", tk.END),edit_window))
        save_button.pack()

    def show_info_message(self, title, message):
        messagebox.showinfo(title, message)
