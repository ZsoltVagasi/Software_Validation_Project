import employee_manager
import relations_manager
import employee
import datetime

def test_if_the_salary_of_an_employee_is_corect_PASS():
    test_relations = relations_manager.RelationsManager()
    test_employee = employee.Employee(id=9, first_name="NotJohn", last_name="NotDoe", base_salary=1000, birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1998, 10, 10))
    test_employee_manager = employee_manager.EmployeeManager(test_relations)
    salary = test_employee_manager.calculate_salary(test_employee)
    assert(salary == 3000)