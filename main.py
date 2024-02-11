import tkinter as tk


def save_password(username, password):
    print("will save new password and a new text file containing pass")

def create_file():
    username = username_entry.get()
    print("if passfile available then check if it matches or not otherwise use save pass func to create a password containg text file")
    #save_password(username, password)

    print("then in username.txt file we will have permission to write the journal")


    write_window = tk.Toplevel(root)
    write_window.title(f"{username}'s Journal.txt")

    def save_content():
       
       print("after clicking save button it will write it to username.txt")

    text_area = tk.Text(write_window)
    text_area.pack(fill="both", expand=True)

    save_button = tk.Button(write_window, text="Save", command=save_content)
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

