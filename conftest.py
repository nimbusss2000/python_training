

from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    host_ip = request.config.getoption('--hostip')

    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, host_ip=host_ip)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url, host_ip=host_ip)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

# разделили фиксуру на две части: инициализацию и финализацию
# (финализ. будет выполняться один раз в самом конце)

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/group.php')
    parser.addoption('--hostip', action='store', default='127.0.0.1')


