from pages.base_page import BasePage
from pages.header import Header
from constants.news_page import NewsPageConst
from pages.utils import log_wrapper, wait_until_ok


class NewsPage(BasePage):
    """Stores methods describes News Page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = NewsPageConst
        self.header = Header(self.driver)

    @log_wrapper
    @wait_until_ok
    def navigate_to_articles_page(self):
        """Navigate to Articles Page via clik on All Articles Link"""
        self.click(xpath=self.const.ALL_ARTICLES_LINK_XPATH)

        from pages.articles_page import ArticlesPage
        return ArticlesPage(self.driver)