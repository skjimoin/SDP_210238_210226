import pytest
import os
from Model.journal_model import Model

@pytest.fixture
def model():
    return Model()

def test_delete_entry_valid_index(model):

    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    model.delete_entry(1)

    with open("journal.txt", "r") as file:
        lines = file.readlines()
    assert lines == ["Entry 1\n", "Entry 3"]

def test_delete_entry_invalid_index(model):

    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    model.delete_entry(5)

    with open("journal.txt", "r") as file:
        lines = file.readlines()
    assert lines == ["Entry 1\n", "Entry 2\n", "Entry 3"]

def test_delete_entry_negative_index(model):
    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    model.delete_entry(-1)

    with open("journal.txt", "r") as file:
        lines = file.readlines()
    assert lines == ["Entry 1\n", "Entry 2\n", "Entry 3"]

