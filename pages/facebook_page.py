from pages.base_page import BasePage
from constants.facebook_page import FacebookPageConsts

from pages.utils import log_wrapper


class FacebookPage(BasePage):
    """Stores methods describes Facebook Page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = FacebookPageConsts

    @log_wrapper
    def verify_to_facebook_page_successful_transition(self):
        """Verify that Facebook Page transition is successful"""
        assert self.is_element_exists(xpath=self.const.FACEBOOK_LOGO_XPATH)
        assert self.is_element_exists(xpath=self.const.FOCUS_IMG_XPATH)