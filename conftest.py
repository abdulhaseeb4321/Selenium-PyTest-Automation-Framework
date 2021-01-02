from pytest import fixture
from utilities.driver import Driver

global driver,browser
@fixture(params=Driver.browser_list)
def setup(request):
    global driver,browser
    driver = Driver(request.param).driver
    browser = request.param
    try:
        yield {'driver': driver, 'browser': request.param}
    except Exception as e:
        print(e)
    finally:
        driver.quit()
