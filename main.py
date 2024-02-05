import tkinter as tk
from tkinter import messagebox

def show_signup_page():
    printf("signup")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        messagebox.showinfo("Login", "Login Done!")
    else:
        messagebox.showerror("Login Error", "Invalid!!!!!!!! give username and password")

root = tk.Tk()
root.title("Login Page")

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
