
from model.group import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_group(Group(name="new_gr", header="new_hea", footer="new_foo"))
    app.session.logout()