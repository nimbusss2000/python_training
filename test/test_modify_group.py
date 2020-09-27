
from model.group import Group
import random


def test_modify_name_some_group_json(app, db, json_groups, check_ui):
    if app.group.count() == 0:
        app.group.create(json_groups)
    grp = json_groups
    old_groups = db.get_group_list()
    some_grp = random.choice(old_groups)
    index = old_groups.index(some_grp)
    grp.id = some_grp.id
    app.group.modify_group_by_id(grp.id, grp)
    assert len(old_groups) == app.group.count()
    old_groups[index] = grp
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_name_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name='group_for_mod'))
    grp = Group(name="new_gr")
    old_groups = db.get_group_list()
    some_grp = random.choice(old_groups)
    index = old_groups.index(some_grp)
    grp.id = some_grp.id
    app.group.modify_group_by_id(grp.id, grp)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = grp
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_header_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='group_for_mod'))
#     old_groups = app.group.get_group_list()
#     app.group.modify_group(Group(header="new_hea"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)




