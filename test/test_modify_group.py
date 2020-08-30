
from model.group import Group

def test_modify_first_group(app):
    app.group.modify_group(Group(name="new_gr", header="new_hea", footer="new_foo"))
