import pytest
from tkinter import Tk, Label

def rock_command(label):
    label.config(text="You = rock")

def paper_command(label):
    label.config(text="You = paper")

def scissors_command(label):
    label.config(text="You = scissors")

@pytest.fixture
def setup():
    window = Tk()
    label3 = Label(window, text="You = ???")
    label3.pack()
    yield window, label3
    window.destroy()

def test_rock_command(setup):
    window, label3 = setup
    rock_command(label3)
    assert label3.cget("text") == "You = rock"

def test_paper_command(setup):
    window, label3 = setup
    paper_command(label3)
    assert label3.cget("text") == "You = paper"

def test_scissors_command(setup):
    window, label3 = setup
    scissors_command(label3)
    assert label3.cget("text") == "You = scissors"
