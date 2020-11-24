from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_have_no_products(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCT_LIST), "Product list is present"

    def should_have_a_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_MESSAGE), "There's no message"
