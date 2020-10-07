
import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT group_id, group_name, group_header, group_footer FROM group_list')
            for row in cursor:
                (id, name, header, footer) = row    # так как каждая строка является кортежем, значения присвоятся сразу в 4 переменные
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list


    def get_contacts_list(self):
        c_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT id, firstname, lastname, middlename, address, home, work, mobile, '
                           'email, email2, email3  FROM addressbook WHERE deprecated="0000-00-00 00:00:00"')
            for row in cursor:
                (id, firstname, lastname, middlename, address, home, work, mobile, email1, email2, email3) = row
                c_list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, homephone=home,
                                      workphone=work, mobilephone=mobile, address_from_hp=address,
                                      email1=email1, email2=email2, email3=email3))
        finally:
            cursor.close()
        return c_list


    def destroy(self):
        self.connection.close()