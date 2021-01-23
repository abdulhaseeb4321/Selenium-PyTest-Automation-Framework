import pytest
from utilities.driver import Driver
from utilities.screenshot import Screenshot
import allure

global driver, browser
import base64


@pytest.fixture(params=Driver.browser_list)
def setup(request):
    global driver, browser
    driver = Driver(request.param).driver
    browser = request.param
    try:
        yield {'driver': driver, 'browser': request.param}
    except Exception as e:
        print(e)
    finally:
        driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    print(extra)
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            if Screenshot.fail_screen_shot_path is not None:
                with open(Screenshot.fail_screen_shot_path['fail_path'], "rb") as img_file:
                    extra.append(pytest_html.extras.image(base64.b64encode(img_file.read()).decode('utf-8'), ''))
                with open(Screenshot.fail_screen_shot_path['base_path'], "rb") as img_file:
                    extra.append(pytest_html.extras.image(base64.b64encode(img_file.read()).decode('utf-8'), ''))

                allure.attach.file(Screenshot.fail_screen_shot_path['fail_path'], name="fail_screenshot",
                                   attachment_type=allure.attachment_type.PNG)
                allure.attach.file(Screenshot.fail_screen_shot_path['base_path'], name="base_screenshot",
                                   attachment_type=allure.attachment_type.PNG)
                Screenshot.fail_screen_shot_path = None
            else:
                screenshot = driver.get_screenshot_as_base64()
                extra.append(pytest_html.extras.image(screenshot, ''))
                allure.attach(driver.get_screenshot_as_png(), name="screenshot",
                              attachment_type=allure.attachment_type.PNG)
    report.extra = extra
