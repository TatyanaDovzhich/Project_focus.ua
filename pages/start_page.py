from constants.start_page import StartPageConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper


class StartPage(BasePage):
    """Stores methods describes Start Page actions"""
    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConsts

    @log_wrapper
    def verify_logo_exists(self):
        """Verify that Logo is present on Start Page"""
        assert self.is_element_exists(xpath=self.const.FOCUS_LOGO_XPATH)

