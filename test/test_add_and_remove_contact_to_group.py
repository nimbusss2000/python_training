
from model.contact import Contact
from model.group import Group
import random

def test_add_c_to_g(app, db, orm):
    groups = db.get_group_list()
    some_group = random.choice(groups)
    if len(groups) == 0:
        app.group.create(Group(name='group_test'))
    contacts = db.get_contacts_list()
    if len(contacts) == 0:
        app.contact.create_contact(Contact(firstname='contact_test'))
    some_contacts = orm.get_contacts_not_in_group(some_group)

    if len(some_contacts) == 0:
        app.contact.create_contact(Contact(firstname='contact_test'))

    some_contact = random.choice(some_contacts)
    old_list_c_in_g = orm.get_contacts_in_group(some_group)
    app.contact.add_contact_to_group(some_contact.id, some_group.id)

    new_list_c_in_g = orm.get_contacts_in_group(some_group)
    assert len(old_list_c_in_g) + 1 == len(new_list_c_in_g)
    old_list_c_in_g.append(some_contact)
    assert sorted(old_list_c_in_g, key=Contact.id_or_max) == sorted(new_list_c_in_g, key=Contact.id_or_max)


def test_remove_c_to_g(app, db, orm):
    groups = db.get_group_list()
    some_group = random.choice(groups)
    if len(groups) == 0:
        app.group.create(Group(name='group_test'))
    contacts = db.get_contacts_list()
    if len(contacts) == 0:
        app.contact.create_contact(Contact(firstname='contact_test'))
    some_contact = random.choice(contacts)
    contacts_in_group = orm.get_contacts_in_group(some_group)

    if len(contacts_in_group) == 0:
        app.contact.add_contact_to_group(some_contact.id, some_group.id)
        contacts_in_group = orm.get_contacts_in_group(some_group)

    contact_for_remove = random.choice(contacts_in_group)
    old_list_c_in_g = orm.get_contacts_not_in_group(some_group)
    app.contact.remove_contact_from_group(contact_for_remove.id, some_group.id)
    new_list_c_in_g = orm.get_contacts_not_in_group(some_group)
    assert len(old_list_c_in_g) + 1 == len(new_list_c_in_g)
    new_list_c_in_g.remove(contact_for_remove)
    assert sorted(old_list_c_in_g, key=Contact.id_or_max) == sorted(new_list_c_in_g, key=Contact.id_or_max)
