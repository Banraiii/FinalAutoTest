from .pages.product_page import ProductPage
#from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import time
import pytest


def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
	page = ProductPage(driver, link)
	page.open()
	page.should_be_basket_button()
	page.go_to_the_basket_in_havbar()
	basket_page = BasketPage(driver, driver.current_url)
	basket_page.should_not_be_item_in_basket()
	basket_page.should_be_message_on_empty_bucket()