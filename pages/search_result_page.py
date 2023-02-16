from pages.base_page import BasePage

from constants.search_result_page import SearchResultPageConsts
from pages.utils import log_wrapper

class SearchResultPage(BasePage):
    """Stores methods describes Search Result Page actions"""
    def __init__(self, driver):
        super().__init__(driver)
        self.const = SearchResultPageConsts

    @log_wrapper
    def verify_result_title_exists(self, search_title):
        """Verify Result Title is present on Search Result Page"""
        assert self.compare_element_text(xpath=self.const.SEARCH_RESULT_INPUT_XPATH, text=search_title.lower())