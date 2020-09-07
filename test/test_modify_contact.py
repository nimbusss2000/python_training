
from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname='test for mod'))
    old_contacts = app.contact.get_contacts_list()
    cntct = Contact(firstname='new_firstname', lastname='new_lastname',
                                       homephone='new_homephone', mobilephone='new_mobilephone',
                                       workphone='new_workphone', fax='new_fax')
    app.contact.modify_contact(cntct)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)

    old_contacts[0] = cntct
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

