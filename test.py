from unittest import result
from main import fonc1, fonc2

def test_fonc1():
    input1 = "oui"
    input2 = "l"

    expected1 = 3
    expected2 = 1

    result1 = fonc1(input1)
    result2 = fonc1(input2)

    assert expected1 == result1
    assert expected2 == result2

