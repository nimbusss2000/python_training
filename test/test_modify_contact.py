
from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(firstname='new_firstname', lastname='new_lastname',
                                       homephone='new_homephone',mobilephone='new_mobilephone',
                                       workphone='new_workphone', fax='new_fax'))
    app.session.logout()