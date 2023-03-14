import employee_manager
import relations_manager
import employee
import datetime

def test_if_the_salary_of_an_employee_is_corect_PASS():
    test_relations = relations_manager.RelationsManager()
    test_employee = employee.Employee(id=9, first_name="NotJohn", last_name="NotDoe", base_salary=1000, birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(1998, 10, 10))
    test_employee_manager = employee_manager.EmployeeManager(test_relations)
    salary = test_employee_manager.calculate_salary(test_employee)
    assert(salary == 3500)
    # assert(salary == 3000)

def test_leader_salary_PASS():
    test_relations = relations_manager.RelationsManager()
    test_employee = employee.Employee(id=9, first_name="NotJohn", last_name="NotDoe", base_salary=2000, birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(2008, 10, 10))
    test_employee_manager = employee_manager.EmployeeManager(test_relations)
    test_relations.teams = {
        1: [2, 3],
        4: [5, 6],
        9: [4, 6, 7]
    }
    salary = test_employee_manager.calculate_salary(test_employee)
    assert(salary == 3900)
    # assert(salary == 3600)

def test_calculate_salary_and_send_email_PASS(capfd):
    test_relations = relations_manager.RelationsManager()
    test_employee = employee.Employee(id=9, first_name="NotJohn", last_name="NotDoe", base_salary=2000, birth_date=datetime.date(1970, 1, 31), hire_date=datetime.date(2008, 10, 10))
    test_employee_manager = employee_manager.EmployeeManager(test_relations)
    test_relations.teams.update({9: [1, 2, 3]})
    test_employee_manager.calculate_salary_and_send_email(test_employee)
    captured = capfd.readouterr()
    assert captured.out == "NotJohn NotDoe your salary: 4100 has been transferred to you.\n"
    # assert captured.out == "NotJohn NotDoe your salary: 3600 has been transferred to you.\n"
    