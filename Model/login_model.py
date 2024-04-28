
class Model:
    def __init__(self):
        self.file_path = "Data/login_info.txt"

    def read_entries(self)  :
        with open(self.file_path, "r") as file:
            entries = file.readlines()
        return entries 
     
    def new_user(self, username, password):
        with open(self.file_path, "a") as new_user_info:
                    new_user_info.write("\n")  
                    new_user_info.write(f"{username} {password}")
