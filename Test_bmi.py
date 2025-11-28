import Lab2.bmi as bmi

print ("Test_bmi")

def test_bmi_underweight():
    weight = 50
    height = 1.75
    result = bmi.calculate_bmi(height, weight)
    assert (result == -1)

def test_bmi_normal():
    weight = 70
    height = 1.75
    result = bmi.calculate_bmi(height, weight)
    assert (result == 0)

def test_bmi_overweight():
    weight = 80
    height = 1.75
    result = bmi.calculate_bmi(height, weight)
    assert (result == 1)