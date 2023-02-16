from pages.base_page import BasePage
from pages.raitings_page import RaitingsPage
from constants.archive_page import ArchivePageConst
from pages.utils import log_wrapper


class ArchivePage(BasePage):
    """Stores methods describes Archive Page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = ArchivePageConst
        self.raitings_page = RaitingsPage(self.driver)


    @log_wrapper
    def verify_slide_text_exists(self):
        """Verify that Slide Text 2020 is exists on Archive Page"""
        assert self.is_element_exists(xpath=self.const.H1_XPATH)

    @log_wrapper
    def click_swiper_button_next(self):
        """Click on Swiper Next button"""
        self.click(xpath=self.const.SWIPER_BUTTON_NEXT_XPATH)

    @log_wrapper
    def verify_swiper_button_next_disabled_exists(self):
        """Verify Swiper Button Next Disabled is exists on Archive Page"""
        assert self.is_element_exists(xpath=self.const.SWIPER_BUTTON_NEXT_DISABLED_XPATH)