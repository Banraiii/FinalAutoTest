from selenium.webdriver.common.by import By


class ProductPageLocators():
	ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-add-to-basket")
	MESSAGE_ADD_ALL = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')
	MESSAGE_ADD_STRONG = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in strong')
	H1_FIND = (By.TAG_NAME, 'h1')
	TOTAL_CARD_PRICE = (By.CSS_SELECTOR, '.basket-mini')
	PRICE_ITEM = (By.CSS_SELECTOR, '.col-sm-6 .price_color')

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_LINK_BTN = (By.CSS_SELECTOR, ".btn-group  a.btn.btn-default")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasketPageLocators():
	ITEM_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-title.hidden-xs")
	MESSAGE_EMPTY_ITEM = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators():
	LOGIN_UNDER_URL = 'login'
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_FORM_FIELDS = (By.CSS_SELECTOR, "#register_form .form-control")
	REGISTER_FORM_BTN = (By.CSS_SELECTOR, "#register_form .btn.btn-lg.btn-primary")