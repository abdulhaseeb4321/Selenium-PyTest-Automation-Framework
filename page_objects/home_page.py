from constants.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.screenshot import Screenshot


class HomePage:
    def __init__(self, driver, browser, testcase_name):
        self.driver = driver
        self.testcase_name = testcase_name
        self.browser = browser
        self.locator = Locators(driver).locators.HomePageLocators

        if driver.execute_script("return window.innerWidth") <= 769:
            WebDriverWait(self.driver, 20).until(
                EC.url_contains('amp'))

    def load_home_page(self):
        screen_shot = Screenshot(self.driver, self.browser, self.testcase_name)
        screen_shot.modify_screen_short('load_home_page', load_page=1)

    def click_kyc_identity_verification_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.kyc_identity_verification_link))
        self.driver.execute_script('arguments[0].click()', element)

    def click_background_AML_screening_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.background_AML_screening_link))
        self.driver.execute_script('arguments[0].click()', element)

    def click_facial_biometric_authentication_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.facial_biometric_authentication))
        self.driver.execute_script('arguments[0].click()', element)

    def click_know_your_business_KYB_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.know_your_business_KYB))
        self.driver.execute_script('arguments[0].click()', element)

    def click_video_interview_kYC(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.video_interview_kYC))
        self.driver.execute_script('arguments[0].click()', element)

    def click_get_in_touch_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.get_in_touch_button))
        self.driver.execute_script('arguments[0].click()', element)

    def click_try_free_demo_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.try_free_demo_button))
        self.driver.execute_script('arguments[0].click()', element)

    def click_verify_with_in_seconds_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.verify_with_in_seconds_link))
        self.driver.execute_script('arguments[0].click()', element)

    def click_background_screening_against_1700_watchlists_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.background_screening_against_1700_watchlists))
        self.driver.execute_script('arguments[0].click()', element)

    def click_request_product_demo_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.request_product_demo))
        self.driver.execute_script('arguments[0].click()', element)

    def click_dss_compliant_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.dss_compliant))
        self.driver.execute_script('arguments[0].click()', element)

    def click_gdpr_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.gdpr))
        self.driver.execute_script('arguments[0].click()', element)

    def click_gdpr_qg_link(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locator.gdpr_qg))
        self.driver.execute_script('arguments[0].click()', element)
