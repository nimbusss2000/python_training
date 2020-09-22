# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, json_contacts):
    cntct = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create_contact(cntct)
    assert len(old_contacts) + 1 == app.contact.count()

    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(cntct)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

