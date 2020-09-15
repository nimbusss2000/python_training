# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string('firstname_', 10), lastname=random_string('lastname_', 10),
                    homephone=random_string('homephone', 7),  mobilephone=random_string('mobilephone', 7),
                    workphone=random_string('workphone', 7), fax=random_string('fax', 5)) for i in range(3)]

@pytest.mark.parametrize('cntct', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, cntct):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create_contact(cntct)
    assert len(old_contacts) + 1 == app.contact.count()

    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(cntct)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

