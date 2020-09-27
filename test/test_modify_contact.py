
from model.contact import Contact
import random

def test_modify_some_contact(app, json_contacts, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_contact(json_contacts)
    old_contacts = db.get_contact_list()
    some_contact = random.choice(old_contacts)
    index = old_contacts.index(some_contact)
    cntct = json_contacts
    cntct.id = some_contact.id
    app.contact.modify_contact_by_id(cntct.id, cntct)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = cntct
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

