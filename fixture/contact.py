
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit_contact_creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def change_field_value(self, field_name, text):
        # checking the condition for filling the contact
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('lastname', contact.lastname)
        self.change_field_value('home', contact.homephone)
        self.change_field_value('mobile', contact.mobilephone)
        self.change_field_value('work', contact.workphone)
        self.change_field_value('fax', contact.fax)

    def delete_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_css_selector('.left:nth-child(8) > input').click()
        assert wd.switch_to.alert.text == "Delete 1 addresses?"
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def modify_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # submit edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('index.php') and len(wd.find_elements_by_name('add')) > 0):
            wd.find_element_by_link_text("home page").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('index.php') and len(wd.find_elements_by_name('add')) > 0):
            wd.get("http://localhost/addressbook/index.php")

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            trs = wd.find_elements_by_css_selector('tr[name="entry"]')
            for td in trs:
                tr = td.find_element_by_css_selector('td[class="center"]')
                id = tr.find_element_by_name('selected[]').get_attribute('value')

                td = td.find_elements_by_tag_name('td')
                firstname = td[2].text
                lastname = td[1].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)
