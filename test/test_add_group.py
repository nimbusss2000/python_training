# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group_json(app, json_groups):        # json_groups - загружаем из пакета data, модуля - groups.json
    grp = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(grp)
    assert len(old_groups) + 1 == app.group.count()

    new_groups = app.group.get_group_list()
    old_groups.append(grp)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_add_group(app, data_groups):            # data_groups - загружаем из пакета data, модуля - groups
#     grp = data_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(grp)
#     assert len(old_groups) + 1 == app.group.count()
#
#     new_groups = app.group.get_group_list()
#     old_groups.append(grp)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

