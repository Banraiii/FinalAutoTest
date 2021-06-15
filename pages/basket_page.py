from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators
from selenium.webdriver.common.by import By
import pytest

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), 'Есть элемент в корзине, не должно быть!'

    def should_be_message_on_empty_bucket(self):
        assert self.check_if_basket_have_empty_basket_message(*BasketPageLocators.MESSAGE_EMPTY_ITEM), "Нет сообщение о пустой корзине"