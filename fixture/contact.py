
from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select

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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_css('selected[]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f'input[value="{id}"').click()

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_css_selector('.left:nth-child(8) > input').click()
        assert wd.switch_to.alert.text == "Delete 1 addresses?"
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_css_selector('.left:nth-child(8) > input').click()
        assert wd.switch_to.alert.text == "Delete 1 addresses?"
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def modify_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # submit edit
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # submit edit
        wd.find_element_by_css_selector(f'a[href="edit.php?id={id}"]').click()
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
                all_phones = td[5].text
                all_emails = td[4].text
                address = td[3].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_hp=all_emails,
                                                  address_from_hp=address))
        return list(self.contact_cache)

    def get_contacts_list_by_id(self, cont_id):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            # self.select_contact_by_id(id)
            trs = wd.find_elements_by_css_selector('tr[name="entry"]')
            for td in trs:
                tr = td.find_element_by_css_selector('td[class="center"]')
                id = tr.find_element_by_name('selected[]').get_attribute('value')
                if id == str(cont_id):
                    td = td.find_elements_by_tag_name('td')
                    firstname = td[2].text
                    lastname = td[1].text
                    all_phones = td[5].text
                    all_emails = td[4].text
                    address = td[3].text
                    self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                      all_phones_from_home_page=all_phones,
                                                      all_emails_from_hp=all_emails,
                                                      address_from_hp=address))
                else:
                    continue
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        tds = wd.find_elements_by_css_selector('tr[name="entry"]')[index]
        td = tds.find_elements_by_tag_name('td')[7]
        td.find_element_by_tag_name('a').click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        tds = wd.find_elements_by_css_selector('tr[name="entry"]')[index]
        td = tds.find_elements_by_tag_name('td')[6]
        td.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        fax = wd.find_element_by_name('fax').get_attribute('value')

        email1 = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')

        address = wd.find_element_by_name('address').text
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, fax=fax,
                       email1=email1, email2=email2, email3=email3, address_from_hp=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        mobilephone = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        fax = re.search('F: (.*)', text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax)

    def add_contact_to_group(self,contact_id):
        wd = self.app.wd

        wd.get(f"http://localhost/addressbook/?group=183")
        wd.find_element_by_id(f"{contact_id}").click()
        wd.find_element_by_name("to_group").click()
        # Select(wd.find_element_by_css_selector(f'value="{contact_id}"'))
        Select(wd.find_element_by_name("to_group")).select_by_visible_text("Power of 3")
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_name("add").click()
        # wd.find_element_by_link_text(f'a[href="./?group={contact_id}"').click()
