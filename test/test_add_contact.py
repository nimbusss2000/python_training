# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname='firstname', lastname='lastname', homephone='homephone',
                                    mobilephone='mobilephone', workphone='workphone', fax='fax'))
    app.session.logout()
