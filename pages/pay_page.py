from pages.base_page import BasePage
from constants.pay_page import PayPageConst
from constants.start_page import StartPageConsts

from pages.utils import log_wrapper


class PayPage(BasePage):
    """Stores methods describes Pay Page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = PayPageConst

    @log_wrapper
    def verify_value_text_exists(self):
        """Verify that Amount Message is present on Pay Page"""
        assert self.is_element_exists(xpath=self.const.VALUE_TEXT_XPATH)

    @log_wrapper
    def verify_value_text_compare(self, amount):
        """Verify that Amount Message is present on Pay Page"""
        assert self.compare_element_text(xpath=self.const.VALUE_TEXT_XPATH, text=amount)

    @log_wrapper
    def navigate_to_start_page(self):
        """Navigate to the Start Page don't used Pay Actions"""
        self.click(xpath=self.const.BACK_LINK_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)