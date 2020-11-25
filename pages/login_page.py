from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Login is not in URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(
            *LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD)
        password_repeat = self.browser.find_element(
            *LoginPageLocators.PASSWORD_REPEAT)
        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_repeat.send_keys(password)
        register_button.click()
