from constants.desktop_locators import DesktopLocators
from constants.emulator_locators import EmulatorLocators


class Locators:

    def __init__(self, driver):
        if driver.execute_script("return window.innerWidth") > 769:
            print("Desktop Locators")
            self.locators = DesktopLocators
        else:
            print("Emulator Locators")
            self.locators = EmulatorLocators
