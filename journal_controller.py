import tkinter as tk
from tkinter import messagebox
from journal_model import Model
from journal_view import View
class Jcontroller :
    def __init__(self, root,username):
        self.username = username
        self.model = Model()
        self.view = View(root)
        self.view.set_controller(self)
     
    def create_file(self,content):
        username = self.username
        content = username + " "+ content
        self.model.write_entry(content)
        messagebox.showinfo("Success", f"{username}'s Journal updated.")

    def read_file(self) :
        entries = self.model.read_entries()
        return entries
        
    def edit_entry(self, entry_num):
            original_content = self.model.read_entry(entry_num)
            if original_content is not None:
                self.view.show_edit_window(entry_num, original_content)
            else:
                self.view.show_info_message("Error", "Entry not found")

    def save_edit(self, entry_num, edited_content,master_window):
        edited_content = self.username + " "+edited_content
        success = self.model.edit_entry(entry_num, edited_content)
        if success:
            self.view.show_info_message("Success", "Entry edited successfully")
            master_window.destroy()
            self.view.read_file_from_controller()
        else:
            self.view.show_info_message("Error", "Failed to edit entry")
    
    def delete_entry(self,entry_num):
        self.model.delete_entry(entry_num)  

        


    