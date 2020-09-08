
from model.group import Group

def test_modify_name_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group_for_mod'))
    old_groups = app.group.get_group_list()
    grp = Group(name="new_gr")
    grp.id = old_groups[0].id
    app.group.modify_group(grp)
    assert len(old_groups) == app.group.count()

    new_groups = app.group.get_group_list()
    old_groups[0] = grp
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_header_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='group_for_mod'))
#     old_groups = app.group.get_group_list()
#     app.group.modify_group(Group(header="new_hea"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)