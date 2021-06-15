from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
import math
from .locators import ProductPageLocators, BasePageLocators, MainPageLocators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url

	def open(self):
		self.driver.get(self.url)

	def should_be_basket_button(self):
		assert self.is_element_present(*BasePageLocators.BASKET_LINK_BTN), 'Нет кнопки коризины!'

	def check_if_h1_in_message(self, how, what):
		try:
			if (self.driver.find_element(*ProductPageLocators.H1_FIND).text) == str(self.driver.find_elements(how, what)[0].text):
				return True
			else:
				return False
		except NoSuchElementException:
			return False

	def total_price_shold_be_equal_item_by_css(self, how, what, baskethow, basketwhat):
		text_area = self.driver.find_element(how, what)
		#print(ProductPageLocators.TOTAL_CARD_PRICE)
		try:
			ec = EC.text_to_be_present_in_element((By.CSS_SELECTOR, f'{ basketwhat }'), str(text_area.text))
			WebDriverWait(self.driver, 12).until(ec)

		except NoSuchElementException:
			return False
		return True

	def is_added_to_basket(self, how, what):
		try:
			if 'added to your basket' in str(self.driver.find_elements(how, what)[0].text):
				return True
			else:
				return False
		except NoSuchElementException:
			return False

	def solve_quiz_and_get_code(self):
		alert = self.driver.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.driver.switch_to.alert
			alert_text = alert.text
			print(f"Ваш код: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print('Второго предупреждения не было')

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(how, what)
		except NoSuchElementException:
			return False
		return True

	def is_not_element_present(self, how, what, timeout=4):
		try:
			es = EC.presence_of_element_located((how, what))
			WebDriverWait(self.driver, timeout).until(es)
		except TimeoutException:
			return True
		
		return False

	def is_disappeared(self, how, what, timeout=4):
		try:
			es = EC.presence_of_element_located((how, what))
			WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(es)
		except TimeoutException:
			return False

		return True

	def go_to_the_basket_in_havbar(self):
		link = self.driver.find_element(*BasePageLocators.BASKET_LINK_BTN)
		link.click()

	def go_to_login_page(self):
		link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
		link.click()

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK)

	def check_if_basket_have_empty_basket_message(self, how, what):
		try:
			if 'Your basket is empty' in str(self.driver.find_element(how, what).text):
				return True
			else:
				return False
		except NoSuchElementException:
			return False

	def in_element(self, string, understr):
		if understr in string:
			return True
		else:
			return False

	def completion_email_fields(self, how, what, email):
		try:
			field = self.driver.find_elements(how, what)[0]
			field.send_keys(f'{ email }')
		except NoSuchElementException:
			return False
		return True 

	def completion_password_fields(self, how, what, password):
		try:
			field = self.driver.find_elements(how, what)[1]
			field.send_keys(f'{ password }')
		except NoSuchElementException:
			return False
		return True 


	def completion_repeat_password_fields(self, how, what, password):
		try:
			field = self.driver.find_elements(how, what)[2]
			field.send_keys(f'{ password }')
		except NoSuchElementException:
			return False
		return True 


	def click_on_buttob(self, how, what):
		try:
			btn = self.driver.find_element(how, what)
			btn.click()
		except NoSuchElementException:
			return False
		return True 