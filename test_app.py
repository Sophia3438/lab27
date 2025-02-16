# test_app.py
import pytest
from prak27 import record, read_balance, readd
from unittest.mock import patch
import os


# Тест для функції record
def test_record():
    record(100)
    with open("text.txt", "r") as file:
        content = file.read()
    assert content == "100"


# Тест для функції read_balance
def test_read_balance():
    record(100)
    assert read_balance() == 100.0

    os.remove("text.txt")
    assert read_balance() == 0.0


# Тест для функції readd
@patch("builtins.input", side_effect=["100", "23", "32221", ""])
def test_readd(mock_input):
    record(100)
    readd("в")
    assert read_balance() == 1285.0

    record(1285)
    readd("д")
    assert read_balance() == 33506.0
