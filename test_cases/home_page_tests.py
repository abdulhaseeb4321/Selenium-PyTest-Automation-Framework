from pytest import mark,fixture
import inspect
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.home_page import HomePage
from constants.urls import Urls

class HomePageTests:

    # @mark.all
    # @mark.home_page
    def test_load_home_page(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)
        home_page = HomePage(driver, browser, testcase_name)
        home_page.load_home_page()

    @mark.all
    @mark.home_page
    def test_click_kyc_identity_verification_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############
        driver.get(Urls.home_page)
        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_kyc_identity_verification_link()
        time.sleep(3)
        assert WebDriverWait(driver, 10).until(EC.url_contains(Urls.identity_verification))

    @mark.all
    @mark.home_page
    def test_click_background_AML_screening_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############
        driver.get(Urls.home_page)
        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_background_AML_screening_link()
        time.sleep(3)
        assert WebDriverWait(driver, 10).until(EC.url_contains(Urls.aml))


    @mark.all
    @mark.home_page
    def test_click_facial_biometric_authentication_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############
        driver.get(Urls.home_page)
        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_facial_biometric_authentication_link()
        time.sleep(3)
        assert WebDriverWait(driver, 10).until(EC.url_contains(Urls.biometric_authentication))


    @mark.all
    @mark.home_page
    def test_click_know_your_business_KYB_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_know_your_business_KYB_link()
        time.sleep(3)
        assert WebDriverWait(driver, 10).until(EC.url_contains(Urls.know_your_business))


    @mark.all
    @mark.home_page
    def test_click_video_interview_kYC(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_video_interview_kYC()
        time.sleep(3)
        assert WebDriverWait(driver, 10).until(EC.url_contains(Urls.video_kyc))


    @mark.all
    @mark.home_page
    def test_click_get_in_touch_button(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_get_in_touch_button()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.contact_us in driver.current_url

    @mark.all
    @mark.home_page
    def test_click_try_free_demo_button(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_try_free_demo_button()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.try_now in driver.current_url

    @mark.all
    @mark.home_page
    def test_click_verify_with_in_seconds_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_verify_with_in_seconds_link()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.quick_verification in driver.current_url

    @mark.all
    @mark.home_page
    def test_click_background_screening_against_1700_watchlists_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_background_screening_against_1700_watchlists_link()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.download_aml_dataset_report in driver.current_url

    @mark.all
    @mark.home_page
    def test_click_request_product_demo_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_request_product_demo_link()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.try_now in driver.current_url

    @mark.all
    @mark.home_page
    def test_click_dss_compliant_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_dss_compliant_link()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.pci in driver.current_url

    @mark.all
    @mark.home_page
    @mark.current

    def test_click_gdpr_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_gdpr_link()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.gdpr in driver.current_url

    @mark.all
    @mark.home_page
    @mark.current
    def test_click_gdpr_qg_link(self, setup):
        driver = setup['driver']
        browser = setup['browser']
        testcase_name = inspect.stack()[0][3]
        ###############initialize constants###############

        driver.get(Urls.home_page)

        home_page = HomePage(driver, browser, testcase_name)
        home_page.click_gdpr_qg_link()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        assert Urls.gdpr_qg in driver.current_url

