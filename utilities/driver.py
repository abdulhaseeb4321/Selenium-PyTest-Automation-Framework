from pathlib import Path
from selenium import webdriver


class Driver:
    browser_list = [
        'chrome',
        # 'firefox',
        # 'Galaxy S5',
        # 'iPhone X',
    ]

    def __init__(self, browser):
        self.browser = browser
        self.driver = self.make_driver()

    def make_driver(self):
        if self.browser == 'chrome':
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.add_argument('--start-maximized')
            return webdriver.Chrome(executable_path=str(Path(__file__).parent.parent) + '/drivers/chromedriver',
                                    options=chrome_opt)

        elif self.browser == 'firefox':
            firefox_opt = webdriver.FirefoxOptions()
            return webdriver.Firefox(executable_path=str(Path(__file__).parent.parent) + '/drivers/geckodriver',
                                     options=firefox_opt)
        elif self.browser != 'chrome' or self.browser != 'firefox':
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.add_argument('--start-maximized')
            chrome_opt.add_experimental_option("mobileEmulation", {"deviceName": self.browser})
            return webdriver.Chrome(executable_path=str(Path(__file__).parent.parent) + '/drivers/chromedriver',
                                    options=chrome_opt)
