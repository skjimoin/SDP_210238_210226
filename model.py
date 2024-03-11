
import os

class JournalModel:
   
    def save_password(username, password):
        with open(f"{username}pass.txt", "w") as pass_file:
            pass_file.write(password)

    
    def get_password(username):
        if os.path.exists(f"{username}pass.txt"):
            with open(f"{username}pass.txt", "r") as pass_file:
                return pass_file.read().strip()
        else:
            return None

    
    def save_entry(username, content):
        file_path = f"{username}.txt"
        with open(file_path, "a") as file:
            file.write(content + '\n')

    
    def get_entries(username):
        file_path = f"{username}.txt"
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return file.readlines()
        else:
            return []
