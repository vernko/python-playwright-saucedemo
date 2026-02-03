"""
Tests for shopping cart functionality.
Tests adding items, removing items, and cart state.
"""

from playwright.sync_api import Page, expect
from tests.helpers.constants import (
    CART_BADGE,
    CART_ITEM,
    CART_LINK,
    REMOVE_BUTTON,
)
from tests.helpers.helpers import add_item_to_cart

def test_add_item_to_cart(authenticated_page: Page):
    """Test adding a product to the cart"""
    add_item_to_cart(authenticated_page)

    expect(authenticated_page.locator(CART_BADGE)).to_have_text("1")

    authenticated_page.click(CART_LINK)
    expect(authenticated_page.locator(CART_ITEM)).to_be_visible()

def test_remove_item_from_cart(authenticated_page: Page):
    """Test removing a product from the cart"""
    add_item_to_cart(authenticated_page)
    expect(authenticated_page.locator(CART_BADGE)).to_have_text("1")

    authenticated_page.click(CART_LINK)
    expect(authenticated_page.locator(CART_ITEM)).to_be_visible()

    authenticated_page.locator(REMOVE_BUTTON).click()
    expect(authenticated_page.locator(CART_ITEM)).not_to_be_visible()

def test_add_multiple_items_to_cart(authenticated_page: Page):
    """Test adding multiple products to the cart"""
    add_item_to_cart(authenticated_page)
    add_item_to_cart(authenticated_page, 1)
    add_item_to_cart(authenticated_page, 2)

    expect(authenticated_page.locator(CART_BADGE)).to_have_text("3")

    authenticated_page.click(CART_LINK)
    expect(authenticated_page.locator(CART_ITEM)).to_have_count(3)