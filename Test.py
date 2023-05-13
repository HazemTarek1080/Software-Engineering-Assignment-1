import pytest
import script


def test_addition():
    assert script.add(5, 10) == 15
    assert script.add(0, 0) == 0
    assert script.add(-5, 5) == 0
    