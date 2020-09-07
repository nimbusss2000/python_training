# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    cntct = Contact(firstname='firstname', lastname='lastname', homephone='homephone',
                                    mobilephone='mobilephone', workphone='workphone', fax='fax')
    app.contact.create_contact(cntct)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(cntct)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

