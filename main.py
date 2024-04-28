
import tkinter as tk
from Controller.login_controller import Login_Controller


def main():
    root = tk.Tk()
    App = Login_Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()