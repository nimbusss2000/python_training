
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init_group_creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit_group_creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def change_field_value(self, field_name, text):
        # checking the condition for filling the group
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.name)
        self.change_field_value('group_footer', group.name)

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('groups').click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name('delete').click()
        self.return_to_groups_page()

    def modify_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit edit
        wd.find_element_by_name('edit').click()
        # change name, header, footer
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()





