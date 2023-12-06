import pytest

import main as  main

def test_add():
    result = main.add(5,5)
    assert result == 10