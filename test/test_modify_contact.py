
from model.contact import Contact
from random import randrange

def test_modify_some_contact(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.create_contact(json_contacts)
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    cntct = json_contacts
    cntct.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, cntct)
    assert len(old_contacts) == app.contact.count()

    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = cntct
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

