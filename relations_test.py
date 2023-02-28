import relations_manager
import datetime

def test_if_john_doe_is_leader_and_check_birtdate_PASS() -> bool:
    test_relations = relations_manager.RelationsManager()
    person = [e for e in test_relations.get_all_employees() if e.first_name == "John" and e.last_name == "Doe"][0]
    assert test_relations.is_leader(person)
    assert(person.birth_date == datetime.date(1970,1,31))

def test_if_myrta_and_jettie_are_members_of_johns_team_members_PASS():
    test_relations = relations_manager.RelationsManager()
    team_leader = [e for e in test_relations.get_all_employees() if e.first_name == "John" and e.last_name == "Doe"][0]
    members = test_relations.get_team_members(team_leader)
    person1 = [e for e in test_relations.get_all_employees() if e.first_name == "Myrta" and e.last_name == "Torkelson"][0]
    person2 = [e for e in test_relations.get_all_employees() if e.first_name == "Jettie" and e.last_name == "Lynch"][0]
    assert (person1.id in members)
    assert (person2.id in members)

def test_if_thomas_andre_is_not_john_does_member_PASS():
    test_relations = relations_manager.RelationsManager()
    team_leader = [e for e in test_relations.get_all_employees() if e.first_name == "John" and e.last_name == "Doe"][0]
    members = test_relations.get_team_members(team_leader)
    person = [e for e in test_relations.get_all_employees() if e.first_name == "Tomas" and e.last_name == "Andre"][0]
    assert(person.id not in members)
    
def test_if_gretchens_salary_is_4000_PASS():
    test_relations = relations_manager.RelationsManager()
    person = [e for e in test_relations.get_all_employees() if e.first_name == "Gretchen" and e.last_name == "Watford"][0]
    assert(person.base_salary == 4000)

def test_if_tomas_andre_is_not_leader_PASS():
    test_relations = relations_manager.RelationsManager()
    person = [e for e in test_relations.get_all_employees() if e.first_name == "Tomas" and e.last_name == "Andre"][0]
    assert not test_relations.is_leader(person)

def test_if_jude_overcash_is_not_in_database_PASS():
    test_relations = relations_manager.RelationsManager()
    employee_first_names = [e.first_name for e in test_relations.get_all_employees()]
    employee_last_names = [e.last_name for e in test_relations.get_all_employees()]
    person_first_name = "Jude"
    person_last_name = "Overcash"
    assert person_first_name not in employee_first_names
    assert person_last_name not in employee_last_names