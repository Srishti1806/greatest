from greatest import max
def test_max_output():
    expected_output = (
        "num1 = 10\n"
        "num2 = 100\n"
        "num3 = 50\n"
        "result = 100\n"
    )
    assert max (num1,num2,num3,result) == expected_output
