from tkinter import messagebox
class Model:
    def __init__(self):
        self.file_path = "journal.txt"

    def read_entries(self)  :
        with open(self.file_path, "r") as file:
            entries = file.readlines()
        return entries   

    def read_entry(self, entry_num):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        if 0 <= entry_num < len(lines):
            return lines[entry_num]
        else:
            return None

    def edit_entry(self, entry_num, edited_content):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        if 0 <= entry_num < len(lines):
            lines[entry_num] = edited_content
            with open(self.file_path, "w") as file:
                file.writelines(lines)
            return True
        else:
            return False
        
    def write_entry(self, content) :
        def is_number(input_value):
            try:
                float(input_value)
                return True
            except ValueError:
                return False
            

        if is_number(content) :
            content = str(content)
        with open(self.file_path, "a") as file:
                
            file.write("\n")  
            if content :        
             file.write(content)

    def delete_entry(self, entry_num):
        if entry_num and entry_num>=0 and entry_num<=self.count_line() :
            with open(self.file_path, "r") as file:
                lines = file.readlines()
            del lines[entry_num]
            with open(self.file_path, "w") as file:
                file.writelines(lines)
        else : return

    def count_line(self) :
        with open(self.file_path, 'r') as file:
            line_count = sum(1 for line in file)
        line_count -= 1
        return line_count
