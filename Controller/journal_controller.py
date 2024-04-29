import tkinter as tk
from tkinter import messagebox
#import Model.journal_model
from Model.journal_model import Model
from View.journal_view import View
class Journal_controller :
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

    def save_edit(self, entry_num, edited_content, master_window):
        edited_content = self.username + " "+edited_content
        success = self.model.edit_entry(entry_num, edited_content)
        if success:
            self.view.show_info_message("Success", "Entry edited successfully")
            master_window.destroy()
            self.view.read_file_from_controller()
        else:
            self.view.show_info_message("Error", "Failed to edit entry")
    
    def delete_entry(self, entry_num):
        self.model.delete_entry(entry_num)  

    def count_reactions(self,username):
        happy_reactions = ["Happy", "happy", "HAPPY", "😁"]
        sad_reactions = ["Sad", "sad", "SAD", "🙁"]
        mixed_sad_reactions = [" not Happy", "not happy", "not HAPPY"]
        mixed_happy_reactions = ["not Sad", "not sad", "not SAD"]
        
        happy_count = 0
        sad_count = 0

        entries = self.model.read_entries()
        for i, entry in enumerate(entries):
                if entry.strip() and entry.strip().split()[0] == username:
                
                    part = entry.split(' ')
                    paragraph = ' '.join(part[1:])
        
                    for reaction in happy_reactions:
                        happy_count += paragraph.count(reaction)
                    for reaction in sad_reactions:
                        sad_count += paragraph.count(reaction)


                    for reaction in mixed_sad_reactions:
                        if reaction in paragraph:
                            
                            sad_count += paragraph.count(reaction)
                            happy_count -= paragraph.count(reaction)
                    for reaction in mixed_happy_reactions:
                        if reaction in paragraph:
                            happy_count += paragraph.count(reaction)
                            sad_count -= paragraph.count(reaction)
        if happy_count > sad_count:
            return "happy"
        elif sad_count > happy_count:
            return "sad"
        else:
            return "neutral"


        


    