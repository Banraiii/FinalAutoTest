from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest


class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, driver):
		link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
		login_page = LoginPage(driver, link)
		login_page.open()
		email = str(time.time()) + "@fakemail.org"
		login_page.register_new_user(email, 'QWer3213ty123')
		login_page.should_be_authorized_user()

	def test_user_can_add_product_to_basket(self, driver):
		link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
		product_page = ProductPage(driver, link)
		product_page.open()
		product_page.shold_be_add_button()
		product_page.add_to_card()
		product_page.shold_be_message_add()

	def test_user_cant_see_success_message(self, driver):
		link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
		product_page = ProductPage(driver, link)
		product_page.open()
		product_page.shold_not_be_message_in_page()