# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname='firstname', lastname='lastname', homephone='homephone',
                                    mobilephone='mobilephone', workphone='workphone', fax='fax'))
    app.session.logout()
