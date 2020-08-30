
from model.group import Group

def test_modify_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group_for_mod'))
    app.group.modify_group(Group(name="new_gr"))

def test_modify_header_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group_for_mod'))
    app.group.modify_group(Group(header="new_hea"))