import pytest
from main import CsvReader

def test_calculate():
    assert CsvReader().calculate(1, 2) == 3

# divide by zero error
def test_divide_error():
    with pytest.raises(ZeroDivisionError):
        CsvReader().divide(1, 0)