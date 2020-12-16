import pytest
from pytest import fixture
from utilities.driver import Driver



@fixture(params=Driver.browser_list, scope='session')
def setup(request):
    driver = Driver(request.param).driver
    try:
        yield {'driver': driver, 'browser': request.param}
    except Exception as e:
        print(e)
    finally:
        driver.quit()


@fixture(scope="session", autouse=True)
def send_report(request):
    print("Test")
