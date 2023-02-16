"""Tests related to header"""

import pytest
import logging

from constants.base import BaseConstants

from constants.header import HeaderConsts
from constants.raitings_page import RaitingsPageConst
from constants.archive_page import ArchivePageConst
from constants.news_page import NewsPageConst
from constants.articles_page import ArticlesPageConst
from constants.donate_page import DonatePageConst
from constants.food_page import FoodPageConsts


@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestHeader:
    """Stores tests for header base functionality"""

    log = logging.getLogger("[TestHeader]")

    def test_raitings_link(self, header, value):
        """
        - Pre-conditions:
            - Open Start Page
            - Navigate to header
        - Steps:
            - Navigate to Raitings Page via clik on Raitings Link
            - Navigate to Archive Page
            - Verify result
            - Click on Swiper Next button for the ending swipper slide
            - Verify result
        """
        # Navigate to Raitings Page via clik Raitings Link
        raitings_page = header.navigate_to_raitings_page()

        # Navigate to Archive 2020 Page
        archive_page = raitings_page.navigate_to_archive_page()

        # Verify result
        archive_page.verify_slide_text_exists

        # Click on Swiper Next button for the ending swipper slide
        for value in range(6):
            value = archive_page.click_swiper_button_next()

        # Verify result
        archive_page.verify_swiper_button_next_disabled_exists()


    def test_all_news_link(self, header):
        """
        - Pre-conditions:
            - Open Start Page
            - Navigate to header
        - Steps:
            - Navigate to News Page via clik on All News Link
            - Navigate to Articles Page
            - Verify result
        """
        # Navigate to News Page via clik All News Link
        news_page = header.navigate_to_news_page()

        # Navigate to Articles Page
        articles_page = news_page.navigate_to_articles_page()

        # Verify result
        articles_page.verify_head_text_exists()

    def test_support_us_button(self, header):
        """
        - Pre-conditions:
            - Open Start Page
            - Navigate to header
        - Steps:
            - Navigate to Donate Page via clik on Support Us button
            - Click on support-form_row' label
            - Navigate to the Pay Page
            - Verify result of navigation to the Pay Page
            - Navigate to the Start Page don't used Pay Actions
            - Verify result of navigation to the Start Page
        """
        # Navigate to Donate Page via clik on Support Us button
        donate_page = header.navigate_to_donate_page()

        # Click on support-form_row' label
        donate_page.click_donate_label()

        # Navigate to the Pay Page
        pay_page = donate_page.navigate_to_pay_page()

        # Verify result of navigation to the Pay Page
        pay_page.verify_value_text_exists()

        # Navigate to the Start Page don't used Pay Actions
        start_page = pay_page.navigate_to_start_page()

        # Verify result of navigation to the Start Page
        start_page.verify_logo_exists()

        def test_support_focus_link(self, header, amount):
            """
            - Pre-conditions:
                - Open Start Page
                - Navigate to header
            - Steps:
                - Navigate to Donate Page via clik on Support Focus link
                - Fill field in amount
                - Navigate to the Pay Page
                - Verify result of navigation to the Pay Page
                - Navigate to the Start Page don't used Pay Actions
                - Verify result of navigation to the Start Page
            """
            # Navigate to Donate Page via clik on Support Focus link
            donate_page = header.navigate_to_donate_page_via_support_link()

            # Fill field in amount & Navigate to the Pay Page after clicking on Support Redaction button
            pay_page = donate_page.support_redaction_button()

            # Verify result of navigation to the Pay Page
            pay_page.verify_value_text_compare(sum=amount.amount)

            # Navigate to the Start Page don't used Pay Actions
            start_page = pay_page.navigate_to_start_page()

            # Verify result of navigation to the Start Page
            start_page.verify_logo_exists()


    def test_search(self, header, search_title):
        """
        - Pre-conditions:
            - Open Start Page
            - Navigate to header
        - Steps:
            - Click on Search button
            - Fill Search field
            - Navigate to the Search Result Page after clicking on Submit button
            - Verify result of search to the Search Result Page
        """
        # Click on Search button
        search_js_window = header.navigate_to_search_js_window()

        # Fill Search field & Navigate to the Search Result Page after clicking on Submit button
        search_result_page = search_js_window.submit_button()

        # Verify result of search to the Search Result Page
        search_result_page.verify_result_title_exists(title=search_title.title)

    def test_yet_drop_down_button(self, header):
        """
        - Pre-conditions:
            - Open Start Page
            - Navigate to header
        - Steps:
            - Click on Yet Drop Down button
            - Navigate to Food page via clicking Food Link
            - Verify result
        """
        # Click on Yet Drop Down button
        header.click_yet_drop_down_button()

        # Navigate to Food page via clicking Food Link
        food_page = header.navigate_to_food_page()

        # Verify result
        food_page.verify_h1_title_exists()

















