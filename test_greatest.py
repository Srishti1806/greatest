from greatest import max
def test_max_output():
    Num1 = 10
    Num2 = 100
    Num3 = 50
    expected_output = (
        "Num1 = 10\n"
        "Num2 = 100\n"
        "Num3 = 50\n"
        "Result = 100\n"
    )
    assert max (Num1, Num2, Num3, Result) == expected_output
