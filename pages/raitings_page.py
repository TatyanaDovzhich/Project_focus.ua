from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper, wait_until_ok


class RaitingsPage(BasePage):
    """Stores methods describes Raitings Page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = RaitingsPageConsts
        self.header = Header(self.driver)

    @log_wrapper
    @wait_until_ok
    def navigate_to_archive_page(self):
        """Navigate to Archive 2020 Page via clik Archive 2020 CTA """
        self.click(xpath=self.const.ARCHIVE_2020_CTA_XPATH)

        from pages.archive_page import ArchivePage
        return ArchivePage(self.driver)