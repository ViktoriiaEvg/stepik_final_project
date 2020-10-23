from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_BUTTON), "Add to basket button is not present"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def compare_cost(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE)
        assert product_price.text == basket_price.text, "The prices aren't equal"

    def compare_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        basket_name = self.browser.find_element(
            *ProductPageLocators.BASKET_NAME)
        assert product_name.text == basket_name.text, "The names don't match"
