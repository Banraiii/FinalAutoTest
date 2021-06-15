from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.in_element(self.driver.current_url, LoginPageLocators.LOGIN_UNDER_URL), 'Не верный url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'нет формы входа'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Нет формы регистрации'

    def register_new_user(self, email, password):
        assert self.completion_email_fields(*LoginPageLocators.REGISTER_FORM_FIELDS, email),\
        "Нет поля формы регистрации email"
        assert self.completion_password_fields(*LoginPageLocators.REGISTER_FORM_FIELDS, password),\
        "Нет поля формы регистрации пороля"
        assert self.completion_repeat_password_fields(*LoginPageLocators.REGISTER_FORM_FIELDS, password),\
        "Нет поля формы регистрации второго пороля"
        assert self.click_on_buttob(*LoginPageLocators.REGISTER_FORM_BTN),\
        "Нет кнопки submit"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"