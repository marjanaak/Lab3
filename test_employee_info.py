import employee_info

def test_get_employees_by_age_range():
    test_employee_data = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ] # expected employees in this age range
    result = employee_info.get_employees_by_age_range(29, 33) # range 29 to 33
    assert (result == test_employee_data) # expecting 2 employees in this age range alice(30) and Bob(35)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    expected_average_salary = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert (result == expected_average_salary) # expected average salary

def test_get_employees_by_dept():
    test_employee_data = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ] # expected employees in Marketing department
    result = employee_info.get_employees_by_dept("Marketing") # department Marketing
    assert (result == test_employee_data) # expecting 2 employees in Marketing department Jane and Mary