from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given('a contact with <firstname> and <lastname>', target_fixture='new_contact')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)

@when('I add a contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create_contact(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_list(app, db, contact_list, new_contact, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(app, db):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname='firstname_for_del'))
    return db.get_contact_list()

@given('a random contact in list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact in list')
def delete_random_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_list(app, db, non_empty_contact_list, random_contact, check_ui):
    new_contacts = db.get_contact_list()
    old_contacts = non_empty_contact_list
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
