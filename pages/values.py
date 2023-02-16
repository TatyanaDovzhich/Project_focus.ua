"""Stores value objects related to the product"""
from pages.utils import random_str, random_num

class SearchTitle:
    def __init__(self, search_title=""):
        self.search_title = search_title

    def fill_data(self):
        """Fill search data by random string"""
        self.search_title = random_str(10)

    def __repr__(self):
        return f"Search Title:(title={self.search_title})"

class Amount:
    def __init__(self, amount=""):
        self.amount = amount

    def fill_data(self):
        """Fill amount data by random number"""
        self.amount = random_num(6)
4
    def __repr__(self):
        return f"Amount:(sum={self.amount})"