from selenium.webdriver.common.by import By


class EmulatorLocators:

    class HomePageLocators:
        # =============================================================================
        # ===============================Home Page Locators Locators===============================
        # =============================================================================
        cookie_notice_button = (By.XPATH, "//a[@id='cn-accept-cookie']")
        kyc_identity_verification_link = (
            By.XPATH,
            '//*[@id="home-section-sp-1-mbl"]//a[contains(text(),"KYC - Identity Verification")]')

        background_AML_screening_link = (
            By.XPATH,
            '//*[@id="home-section-sp-1-mbl"]//a[contains(text(),"Background AML Screening")]')

        facial_biometric_authentication = (
            By.XPATH,
            '//*[@id="home-section-sp-1-mbl"]//a[contains(text(),"Facial Biometric Authentication")]')

        know_your_business_KYB = (
            By.XPATH,
            '//*[@id="home-section-sp-1-mbl"]//a[contains(text(),"Know Your Business - KYB")]')

        video_interview_kYC = (
            By.XPATH, '//*[@id="home-section-sp-1-mbl"]//a[contains(text(),"Video Interview KYC")]')

        ocr_for_business = (
            By.XPATH, '//*[@id="home-section-sp-1-mbl"]//a[contains(text(),"OCR for Business ")]')

        get_in_touch_button = (
            By.XPATH, "//div[not(contains(@id,'hm-btn-bnner-c'))]/a[contains(text(),'Get in Touch')]"
        )
        try_free_demo_button = (
            By.XPATH, "//div[contains(@class,'mobile')]//a[contains(text(),'Try Free Demo')]"
        )

        background_screening_against_1700_watchlists = (
            By.XPATH, "//*[@id='home-section-sp-3']//a[contains(@href,'download-aml-dataset-report')]"
        )

        verify_with_in_seconds_link = (
            By.XPATH, "//*[@id='home-section-sp-3']//a[contains(@href,'quick-verification')]"
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
    # ===============================Home Page Locators===============================
    # =============================================================================
