# -*- coding: utf-8 -*-

from model.contact import Contact
import allure


def test_add_contact(app, json_contacts, db, check_ui):
    cntct = json_contacts
    with allure.step('Given a contact with <firstname> and <lastname>'):
        old_contacts = db.get_contact_list()
    with allure.step(f'When I add a {cntct} to the list'):
        app.contact.create_contact(cntct)
    with allure.step(f'Then the new contact list is equal to the old list with the added contact'):
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = db.get_contact_list()
        old_contacts.append(cntct)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == \
                   sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


