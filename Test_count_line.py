from Model.journal_model import Model
import os

def test_count_line():
    temp_file_path = "temp_journal.txt"
    with open(temp_file_path, "w") as file:
        file.write("First line\n")
        file.write("Second line\n")
        file.write("Third line\n")

    model = Model()
    model.file_path = temp_file_path

    assert model.count_line() == 2
    os.remove(temp_file_path)


def test_count_line_if_NULL():
    temp_file_path = "temp_journal_Null.txt"
    with open(temp_file_path, "w") as file:
        file.write("")

    model = Model()
    model.file_path = temp_file_path

    assert model.count_line() == -1
    os.remove(temp_file_path)