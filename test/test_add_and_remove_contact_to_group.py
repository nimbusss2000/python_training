
from model.contact import Contact
import random

def test_add_c_to_g(app, db, orm):
    contacts_list = db.get_contact_list()
    some_contact = random.choice(contacts_list)
    groups_list = db.get_group_list()
    some_group = random.choice(groups_list)
    old_list_c_in_g = orm.get_contacts_in_group(some_group)
    app.contact.add_contact_to_group(some_contact.id, some_group.id)
    new_list_c_in_g = orm.get_contacts_in_group(some_group)
    assert len(old_list_c_in_g) + 1 == len(new_list_c_in_g)
    old_list_c_in_g.append(some_contact)
    assert sorted(old_list_c_in_g, key=Contact.id_or_max) == sorted(new_list_c_in_g, key=Contact.id_or_max)


def test_remove_c_to_g(app, db, orm):
    groups = db.get_group_list()
    some_group = random.choice(groups)
    contacts = orm.get_contacts_in_group(some_group)
    if contacts is None:
        contacts_list = db.get_contact_list()
        some_contact = random.choice(contacts_list)
        app.contact.add_contact_to_group(some_contact.id, some_group.id)
    some_contact = random.choice(contacts)
    old_list_c_in_g = orm.get_contacts_not_in_group(some_group)
    app.contact.remove_contact_from_group(some_contact.id, some_group.id)
    new_list_c_in_g = orm.get_contacts_not_in_group(some_group)
    assert len(old_list_c_in_g) + 1 == len(new_list_c_in_g)
    new_list_c_in_g.remove(some_contact)
    assert sorted(old_list_c_in_g, key=Contact.id_or_max) == sorted(new_list_c_in_g, key=Contact.id_or_max)



