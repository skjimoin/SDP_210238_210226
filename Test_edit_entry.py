import pytest
import os
from journal_model import Model

@pytest.fixture
def model():
    return Model()

def test_edit_entry_valid_index(model):
    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    edit_result = model.edit_entry(1, "Edited Entry")

    assert edit_result is True
    with open("journal.txt", "r") as file:
        lines = file.readlines()
    assert lines[1] == "Edited EntryEntry 3"

def test_edit_entry_invalid_index(model):
    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    edit_result = model.edit_entry(5, "Edited Entry")

    assert edit_result is False

def test_edit_entry_negative_index(model):
    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    edit_result = model.edit_entry(-1, "Edited Entry")

    assert edit_result is False

def test_edit_entry_empty_file(model):
    open("journal.txt", "w").close()

    edit_result = model.edit_entry(0, "Edited Entry")

    assert edit_result is False
