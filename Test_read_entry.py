import pytest
from journal_model import Model

@pytest.fixture
def model():
    return Model()

def test_read_entry_valid_index(model):
    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    entry = model.read_entry(1) 

    assert entry == "Entry 2\n"

def test_read_entry_invalid_index(model):
    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")

    entry = model.read_entry(5)
    assert entry is None

def test_read_entry_negative_index(model):
    with open("journal.txt", "w") as file:
        file.write("Entry 1\nEntry 2\nEntry 3")
    entry = model.read_entry(-1)
    assert entry is None

def test_read_entry_empty_file(model):

    open("journal.txt", "w").close() 

    entry = model.read_entry(0)

    assert entry is None
