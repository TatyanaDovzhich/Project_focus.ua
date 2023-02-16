from pages.base_page import BasePage
from constants.footer import FooterConsts

from pages.utils import log_wrapper


class Footer(BasePage):
    """Stores methods describes footer actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = FooterConsts

    @log_wrapper
    def navigate_to_facebook_page(self):
        """Navigate to the Facebook Page via clicking on Facebook Social Link"""
        self.click(xpath=self.const.FACEBOOK_SOCIAL_LINK_XPATH)

        from pages.facebook_page import FacebookPage
        return FacebookPage(self.driver)