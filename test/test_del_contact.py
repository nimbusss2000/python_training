
from model.contact import Contact
import random
import allure

def test_delete_some_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create_contact(Contact(firstname='firstname_for_del'))
    with allure.step('Given a random contact in list'):
        old_contacts = db.get_contact_list()
        some_contact = random.choice(old_contacts)
    with allure.step(f'When I delete the {some_contact} in list'):
        app.contact.delete_contact_by_id(some_contact.id)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.remove(some_contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == \
                   sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
