import re
import random
import string


def test_all_info_db_contacts(app, db):
    phones_from_home_page = app.contact.get_info_all_phones()
    emails_from_home_page = app.contact.get_info_all_emails()
    contact_from_db = db.get_contacts_list()
    assert sorted(phones_from_home_page) == sorted(merge_phones_like_on_home_page(contact_from_db))
    assert sorted(emails_from_home_page) == sorted(merge_emails_like_on_home_page(contact_from_db))


def test_info_on_home_page(app):
    contacts = app.contact.get_contacts_list()
    index = random.randrange(len(contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_hp == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.fax == contact_from_edit_page.fax


def merge_phones_like_on_home_page(l):
    a = []
    for contact in l:
        a.append('\n'.join(filter(lambda x: x != '',
                                map(lambda x: clean(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobilephone, contact.workphone,])))))
    return a


def merge_emails_like_on_home_page(l):
    a = []
    for contact in l:
        a.append('\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email1, contact.email2, contact.email3])))))
    return a


def clear(s):
   return re.sub("[(-)] -", "", s)


bad_punctuation ='[(-)] '
good_chars = (string.ascii_letters + string.digits + string.punctuation).encode()
bad_chars = bytearray(set(range(0x100)) - set(good_chars)) + bad_punctuation.encode()

def clean(text):
    return text.encode('ascii', 'ignore').translate(None, bad_chars).decode()

