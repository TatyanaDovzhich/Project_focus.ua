from enum import verify
from pages.base_page import BasePage
from constants.header import HeaderConsts
from constants.search_js_window import SearchJSWindowConsts
from constants.food_page import FoodPageConsts

from pages.utils import log_wrapper, wait_until_ok


class Header(BasePage):
    """Stores methods describes header actions"""
    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConsts

    @log_wrapper
    def navigate_to_raitings_page(self):
        """Navigate to Raitings Page via clik Raitings Link on header"""
        self.click(xpath=self.const.RAITINGS_LINK_XPATH)

        from pages.raitings_page import RaitingsPage
        return RaitingsPage(self.driver)

    @log_wrapper
    def navigate_to_news_page(self):
        """Navigate to News Page via clik All News Item on header"""
        self.click(xpath=self.const.ALLNEWS_ITEM_XPATH)

        from pages.news_page import NewsPage
        return NewsPage(self.driver)

    @log_wrapper
    def navigate_to_donate_page(self):
        """Navigate to Donate Page via clik on Support Us button"""
        self.click(xpath=self.const.SUPPORT_US_BUTTON_XPATH)

        from pages.donate_page import DonatePage
        return DonatePage(self.driver)

    @log_wrapper
    def navigate_to_donate_page_via_support_link(self):
        """Navigate to Donate Page via clik on Support Focus Link"""
        self.click(xpath=self.const.SUPPORT_FOCUS_LINK_XPATH)

        from pages.donate_page import DonatePage
        return DonatePage(self.driver)

    @log_wrapper
    def navigate_to_search_js_window(self):
        """Navigate to Search JS Window via click on Search button"""
        self.click(xpath=self.const.SEARCH_BUTTON_XPATH)

        from pages.search_js_window import SearchJSWindow
        return SearchJSWindow(self.driver)

    @log_wrapper
    def click_yet_drop_down_button(self):
        """Click on Yet Drop Down button"""
        self.click(xpath=self.const.YET_DROPDOWN_BUTTON_XPATH)

    @log_wrapper
    def navigate_to_food_page(self):
        """Navigate to Search JS Window via click on Search button"""
        self.click(xpath=self.const.FOOD_DROPDOWN_LINK_XPATH)

        from pages.food_page import FoodPage
        return FoodPage(self.driver)





