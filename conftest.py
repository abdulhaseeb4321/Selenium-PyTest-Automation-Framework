import pytest
from pytest import fixture
from utilities.driver import Driver
from mat import mattermost
count_to_send_report = 0


@fixture(params=Driver.browser_list, scope='session')
def setup(request):
    driver = Driver(request.param).driver
    try:
        yield {'driver': driver, 'browser': request.param}
    except Exception as e:
        print(e)
    finally:
        driver.quit()
    global count_to_send_report
    count_to_send_report += 1
    if count_to_send_report == len(Driver.browser_list)-1:
        f = open("demofile2.txt", "a")
        f.write(str(count_to_send_report) + "\n")
        f.close()
    else:
        f = open("demofile2.txt", "a")
        f.write("not" + "\n")
        f.close()


@fixture(scope="session", autouse=True)
def send_report(request):
    print("Test")
