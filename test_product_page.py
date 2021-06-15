from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function")
	def setup(self, driver):
		link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
		login_page = LoginPage(driver, link)
		login_page.open()
		email = str(time.time()) + "@fakemail.org"
		login_page.register_new_user(email, 'QWer3213ty123')
		login_page.should_be_authorized_user()

	def test_user_can_add_product_to_basket(self, driver, setup):
		link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
		product_page = ProductPage(driver, link)
		product_page.open()
		product_page.shold_be_add_button()
		product_page.add_to_card()
		time.sleep(20)
		product_page.shold_be_message_add()


	def test_user_cant_see_success_message(self, driver, setup):
		link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
		product_page = ProductPage(driver, link)
		product_page.open()
		product_page.shold_not_be_message_in_page()

	
	def test_guest_can_add_product_to_basket(self, driver):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
		product_page = ProductPage(driver, link)
		product_page.open()
		product_page.shold_be_add_button()
		product_page.add_to_card()
		product_page.shold_be_message_add()

	def test_guest_cant_see_product_in_basket_opened_from_product_page(self, driver):
		link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
		page = ProductPage(driver, link)
		page.open()
		page.should_be_basket_button()
		page.go_to_the_basket_in_havbar()
		basket_page = BasketPage(driver, driver.current_url)
		basket_page.should_not_be_item_in_basket()
		basket_page.should_be_message_on_empty_bucket()

	def test_guest_can_go_to_login_page_from_product_page(self, driver):
		link = "http://selenium1py.pythonanywhere.com/en-gb/"
		page = ProductPage(driver, link)
		page.open()
		page.go_to_login_page()