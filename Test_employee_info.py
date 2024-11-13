import employee_info as EI
from employee_info import employee_data as EIDATA

def test_get_employees_by_age_range():
    result = []
    upper = 36
    lower = 29
    expected = 3  
    
    result = len(EI.get_employees_by_age_range(lower, upper))
    assert (result == expected)

    

def test_calculate_average_salary():
    result = None
    expected = 60166.67

    result = EI.calculate_average_salary()
    assert (result == expected)


def get_employees_by_dept():
    result = None
    targetDept = "Marketing"
    expected = [EIDATA[1], EIDATA[2]]
    
    result = EI.get_employees_by_dept(targetDept)

    assert (result == expected)