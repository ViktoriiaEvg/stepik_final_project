from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo', ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_to_basket()
    browser.implicitly_wait(5)
    page.compare_cost()
    page.compare_name()
