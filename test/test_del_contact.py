
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname='firstname_for_del'))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_contact()
    assert len(old_contacts) - 1 == app.contact.count()

    new_contacts = app.contact.get_contacts_list()
    old_contacts = old_contacts[1:]
    assert old_contacts == new_contacts
