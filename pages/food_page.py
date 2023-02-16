from pages.base_page import BasePage
from constants.food_page import FoodPageConsts

from pages.utils import log_wrapper


class FoodPage(BasePage):
    """Stores methods describes Food Page actions"""
    def __init__(self, driver):
        super().__init__(driver)
        self.const = FoodPageConsts

    @log_wrapper
    def verify_h1_title_exists(self):
        """Verify that H1 Title is present on Food Page"""
        assert self.is_element_exists(xpath=self.const.H1_TITLE_XPATH)