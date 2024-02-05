import tkinter as tk
from tkinter import messagebox

def show_signup_page():
    signup_window = tk.Toplevel(root)
    signup_window.title("Journalify")
    signup_window.geometry('800x400')
    signup_window.configure(bg = "#219299")
    
    tk.Label(signup_window, text="Sign Up").pack()

    tk.Label(signup_window, text="Enter your Information").pack()

    tk.Label(signup_window, text="Username:").pack()
    signup_username_entry = tk.Entry(signup_window)
    signup_username_entry.pack()

    tk.Label(signup_window, text="Password:").pack()
    signup_password_entry = tk.Entry(signup_window, show="*")
    signup_password_entry.pack()

    tk.Label(signup_window, text="Confirm Password:").pack()
    confirm_password_entry = tk.Entry(signup_window, show="*")
    confirm_password_entry.pack()

    def perform_signup():
        new_username = signup_username_entry.get()
        new_password = signup_password_entry.get()
        confirm_password = confirm_password_entry.get()

        if new_password == confirm_password:
            messagebox.showinfo("Signup", f"Signup successful for {new_username}!")
            signup_window.destroy()
        else:
            messagebox.showerror("Signup Error", "Password doesn't match")

    signup_button = tk.Button(signup_window, text="Sign Up", command=perform_signup)
    signup_button.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        messagebox.showinfo("Login", "Login Complete!")
    else:
        messagebox.showerror("Login Error", "Invalid! Please give username and password")

root = tk.Tk()
root.title("Journalify")
root.geometry('800x400')
root.geometry("1000x692")
root.configure(bg = "#219299")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

signup_button = tk.Button(root, text="Sign Up", command=show_signup_page)
signup_button.pack()

root.mainloop()


