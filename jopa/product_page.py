from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
import pytest

class ProductPage(BasePage):
	def shold_be_add_button(self):
		assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Нет кнопки добавить в коризину!'

	def add_to_card(self):
		btn = self.driver.find_element(*ProductPageLocators.ADD_BUTTON)
		btn.click()
		self.solve_quiz_and_get_code()

	def shold_be_message_add(self):
		assert self.is_added_to_basket(*ProductPageLocators.MESSAGE_ADD_ALL), 'Нет сообщения о добавлении в карзину'
		assert self.check_if_h1_in_message(*ProductPageLocators.MESSAGE_ADD_STRONG), 'В зоголовке сообщения нет названия товара'
		assert self.total_price_shold_be_equal_item_by_css(*ProductPageLocators.PRICE_ITEM, *ProductPageLocators.TOTAL_CARD_PRICE), 'Не подходит цена и тотал прайс в корзине'

	def shold_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
		"Есть сообщения о добавлении товара, и не должно быть"


	def shold_not_be_message_in_page(self):
		assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_ALL),\
		'Сообщение присутствует о добавлении товара, не должно!'

	def shold_be_disappeared_message(self):
		assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_ALL),\
		'Элемент присутствует на странице и должен исчезнуть'
