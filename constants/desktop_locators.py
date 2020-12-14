from selenium.webdriver.common.by import By


class DesktopLocators:

    class HomePageLocators:
        # =============================================================================
        # ===============================Home Page===============================
        # =============================================================================
        kyc_identity_verification_link = (
            By.XPATH,
            '//*[@id="home-section-sp-1"]//a[contains(text(),"KYC - Identity Verification")]')

        background_AML_screening_link = (
            By.XPATH,
            '//*[@id="home-section-sp-1"]//a[contains(text(),"Background AML Screening")]')

        facial_biometric_authentication = (
            By.XPATH,
            '//*[@id="home-section-sp-1"]//a[contains(text(),"Facial Biometric Authentication")]')

        know_your_business_KYB = (
            By.XPATH,
            '//*[@id="home-section-sp-1"]//a[contains(text(),"Know Your Business - KYB")]')

        video_interview_kYC = (
            By.XPATH, '//*[@id="home-section-sp-1"]//a[contains(text(),"Video Interview KYC")]')

        ocr_for_business = (
            By.XPATH, '//*[@id="home-section-sp-1"]//a[contains(text(),"OCR for Business ")]')

        get_in_touch_button = (
            By.XPATH, "//div[@id='hm-btn-bnner-c']/a[contains(text(),'Get in Touch')]")

        try_free_demo_button = (
            By.XPATH, "//div[@id='countries-new-btn-trynow' and ..//div[@id='hm-btn-bnner-c']]/a[contains(text(),'Try Free Demo')]")

        verify_with_in_seconds_link = (
            By.XPATH, "//*[@id='home-section-sp-3']//a[contains(@href,'quick-verification')]"
        )
        background_screening_against_1700_watchlists = (
            By.XPATH, "//*[@id='home-section-sp-3']//a[contains(@href,'download-aml-dataset-report')]"
        )

        request_product_demo = (
            By.XPATH, "//a[contains(text(),'Request Product Demo')]"
        )

        dss_compliant = (
            By.XPATH, "//div[contains(@id,'home-section-sp-4')]//a[contains(text(),'DSS COMPLIANT')]"
        )

        gdpr = (
            By.XPATH, "//div[contains(@id,'home-section-sp-4')]//a[text()='GDPR']"
        )

        gdpr_qg = (
            By.XPATH, "//div[contains(@id,'home-section-sp-4')]//a[text()='GDPR QG']"
        )

        # =============================================================================
        # ===============================Home Page===============================
        # =============================================================================

