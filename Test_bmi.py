import Lab2.bmi as bmi

def test_bmi_underweight():
    result = None
    height = 2
    weight = 50
    test = -1

    result = bmi.calculate_bmi(height, weight)

    assert (result == test)

def test_bmi_normal_weight():
    result = None
    height = 1.73
    weight = 57
    test = 0

    result = bmi.calculate_bmi(height, weight)

    assert (result == test)

def test_bmi_overweight():
    result = None
    height = 1.3
    weight = 90
    test = 1

    result = bmi.calculate_bmi(height, weight)

    assert (result == test)