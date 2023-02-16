from enum import verify

from constants.search_js_window import SearchJSWindowConsts
from pages.base_page import BasePage
from constants.search_result_page import SearchResultPageConsts
from pages.utils import log_wrapper, wait_until_ok

class SearchJSWindow(BasePage):
    """Stores methods describes Search JS Window actions"""
    def __init__(self, driver):
        super().__init__(driver)
        self.const = SearchJSWindowConsts


    @wait_until_ok (timeout=3, period=0.5)
    def click_and_validate_submit_button(self):
        """Click on Search button until it disappear"""
        self.click(self.const.SUBMIT_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.SUBMIT_BUTTON_XPATH), "Submit button didn't disappear"

    @log_wrapper
    def submit_button(self, search_title, verify=True):
        """Click Submit button after filling search field"""
        # Fill search field
        self.fill_field(xpath=self.const.SEARCH_INPUT_XPATH, value=search_title.title)

        # Click on Submit button
        if verify:
            self.click_and_validate_submit_button()
        else:
            self.click(self.const.SUBMIT_BUTTON_XPATH)

        from pages.search_result_page import SearchResultPage
        return SearchResultPage(self.driver)


