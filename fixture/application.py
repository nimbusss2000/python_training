
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self, browser, base_url, host_ip):
        if browser == 'chrome':
            self.wd = webdriver.Chrome(executable_path=r'C:\gecko\chromedriver1.exe')
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'ie':
            self.wd = webdriver.Ie(executable_path=r'C:\gecko\IEDriverServer.exe')
        else:
            raise ValueError('unrecognized browser')
        self.base_url = base_url
        self.host_ip = host_ip
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()