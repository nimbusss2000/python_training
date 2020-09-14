
import re
import random

def test_emails_on_home_page(app):
    contacts = app.contact.get_contacts_list()
    index = random.randrange(len(contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.all_emails_from_hp == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
   return re.sub("[() -]", "", s)

def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email1, contact.email2, contact.email3]))))