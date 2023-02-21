import relations_manager
import employee
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

    