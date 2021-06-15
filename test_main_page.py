from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest


class TestLoginFromMainPage():
	def test_guest_can_go_to_login_page(self, driver):
		link = "http://selenium1py.pythonanywhere.com"
		page = MainPage(driver, link)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()						# открываем страницу
		page.should_be_login_link()		# выполняем проверку нахождения логин линк
		page.go_to_login_page()			# выполняем метод страницы — переходим на страницу логина
		login_page = LoginPage(driver, driver.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link(self, driver):
		link = "http://selenium1py.pythonanywhere.com"
		page = MainPage(driver, link)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
		page.open()						# открываем страницу
		page.should_be_login_link()		# выполняем проверку нахождения логин линк

def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
	link = "http://selenium1py.pythonanywhere.com/en-gb/"
	page = MainPage(driver, link)
	page.open()
	page.should_be_basket_button()
	page.go_to_the_basket_in_havbar()
	basket_page = BasketPage(driver, driver.current_url)
	time.sleep(2)
	basket_page.should_not_be_item_in_basket()
	basket_page.should_be_message_on_empty_bucket()