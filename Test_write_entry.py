import pytest
import os
from journal_model import Model

@pytest.fixture
def model():
    return Model()

def test_write_entry_text(model):

    test_content = "New Entry"

    model.write_entry(test_content)

    with open("journal.txt", "r") as file:
        lines = file.readlines()
    assert lines[-1] == "New Entry"



def test_write_entry_blank(model):

    test_content = ""

    model.write_entry(test_content)

    with open("journal.txt", "r") as file:
        lines = file.readlines()
    assert lines[-1] != ""


def test_write_entry_number(model):

    test_content = 1234

    model.write_entry(test_content)

    with open("journal.txt", "r") as file:
        lines = file.readlines()
    assert lines[-1] == "1234"



