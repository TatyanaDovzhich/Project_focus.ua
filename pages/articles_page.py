from pages.base_page import BasePage
from pages.news_page import NewsPage
from constants.articles_page import ArticlesPageConst
from pages.utils import log_wrapper, wait_until_ok


class ArticlesPage(BasePage):
    """Stores methods describes Articles Page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = ArticlesPageConst
        self.news_page = NewsPage(self.driver)


    @log_wrapper
    @wait_until_ok
    def verify_head_text_exists(self):
        """Verify that Head Text is exist on Articles Page"""
        assert self.is_element_exists(xpath=self.const.HEAD_XPATH)