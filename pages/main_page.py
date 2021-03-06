from .base_page import BasePage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
import pytest

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
