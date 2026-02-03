"""
Helper functions for cart operations.
"""

from playwright.sync_api import Page
from tests.helpers.constants import (
    PRODUCT_ITEM,
    ADD_TO_CART_BUTTON,
    CART_LINK,
    CHECKOUT_BUTTON,
)

def add_item_to_cart(page: Page, index: int = 0):
    """
    Add a product to cart by index.
    
    Args:
        page: Playwright Page object
        index: Product index to add (default 0 for first product)
    """
    product = page.locator(PRODUCT_ITEM).nth(index)
    product.locator(ADD_TO_CART_BUTTON).click()

def navigate_to_checkout(page: Page):
    """
    Navigate to checkout page.
    
    Args:
        page: Playwright Page object
    """
    page.click(CART_LINK)
    page.click(CHECKOUT_BUTTON)