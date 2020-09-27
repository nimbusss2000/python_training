# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    cntct = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_contact(cntct)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(cntct)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


