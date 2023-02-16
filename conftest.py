import datetime
# import os

import pytest

from constants.base import BaseConstants

from pages.utils import create_driver
from pages.values import SearchTitle


@pytest.fixture()
def driver(browser):
    """Creates selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


# @pytest.fixture()
# def start_page(driver):
#     """Creates start page object"""
#     return StartPage(driver)
#
#
# @pytest.fixture()
# def empty_search_text():
#     """Creates an empty search text"""
#     return SearchText()
#
#
# @pytest.fixture()
# def random_user(empty_user):
#     """Creates random user"""
#     empty_user.fill_data()
#     return empty_user
#
#
@pytest.fixture()
def random_search_title():
    """Creates random search title"""
    search_title = SearchTitle()
    search_title.fill_data()
    return search_title
#
#
# @pytest.fixture()
# def hello_page(start_page, random_user):
#     return start_page.sign_up(random_user)
#
#
# def pytest_sessionstart(session):
#     os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConstants.DRIVER_PATH)}"



