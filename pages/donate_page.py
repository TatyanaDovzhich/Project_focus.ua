from pages.base_page import BasePage
from constants.donate_page import DonatePageConst

from pages.utils import log_wrapper, wait_until_ok


class DonatePage(BasePage):
    """Stores methods describes Donate Page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = DonatePageConst

    @log_wrapper
    def click_donate_label(self):
        """Click on Donate Label (100)"""
        self.click(xpath=self.const.DONATE_100_XPATH)

    @log_wrapper
    def navigate_to_pay_page(self):
        """Navigate to Pay Page via clik on Support Redaction button"""
        self.click(xpath=self.const.SUPPORT_REDACTION_BUTTON_XPATH)

        from pages.pay_page import PayPage
        return PayPage(self.driver)

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_support_redaction_button(self):
        """Click on Support Redaction button until it disappear"""
        self.click(self.const.SUPPORT_REDACTION_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.SUPPORT_REDACTION_BUTTON_XPATH), "Support Redaction button didn't disappear"

    @log_wrapper
    def support_redaction_button(self, amount, verify=True):
        """Click on Support Redaction button after filling amount field"""
        # Fill amount field
        self.fill_field(xpath=self.const.INPUT_AMOUNT_FIELD_XPATH, value=amount.amount)

        # Click on Support Redaction button
        if verify:
            self.click_and_validate_support_redaction_button()
        else:
            self.click(self.const.SUPPORT_REDACTION_BUTTON_XPATH)

        from pages.pay_page import PayPage
        return PayPage(self.driver)