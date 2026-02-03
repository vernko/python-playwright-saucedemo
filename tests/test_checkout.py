"""
Tests for checkout flow.
Tests complete checkout, validation, and cancellation.
"""

from playwright.sync_api import Page, expect
from tests.helpers.constants import (
    CART_URL,
    CART_ITEM,
    FIRST_NAME_INPUT,
    LAST_NAME_INPUT,
    ZIP_CODE_INPUT,
    CONTINUE_BUTTON,
    CHECKOUT_ERROR,
    CANCEL_BUTTON,
    FINISH_BUTTON,
    CHECKOUT_COMPLETE_HEADER,
    TEST_FIRST_NAME,
    TEST_LAST_NAME,
    TEST_ZIP_CODE,
)
from tests.helpers.helpers import add_item_to_cart, navigate_to_checkout

def test_complete_checkout(authenticated_page: Page):
    """Test complete checkout flow from cart to order completion"""
    add_item_to_cart(authenticated_page)
    navigate_to_checkout(authenticated_page)

    authenticated_page.fill(FIRST_NAME_INPUT, TEST_FIRST_NAME)
    authenticated_page.fill(LAST_NAME_INPUT, TEST_LAST_NAME)
    authenticated_page.fill(ZIP_CODE_INPUT, TEST_ZIP_CODE)
    authenticated_page.click(CONTINUE_BUTTON)

    authenticated_page.click(FINISH_BUTTON)
    expect(authenticated_page.locator(CHECKOUT_COMPLETE_HEADER)).to_be_visible()

def test_checkout_empty_first_name(authenticated_page: Page):
    """Test that checkout shows error when first name is empty"""
    add_item_to_cart(authenticated_page)
    navigate_to_checkout(authenticated_page)

    authenticated_page.fill(LAST_NAME_INPUT, TEST_LAST_NAME)
    authenticated_page.fill(ZIP_CODE_INPUT, TEST_ZIP_CODE)
    authenticated_page.click(CONTINUE_BUTTON)

    error = authenticated_page.locator(CHECKOUT_ERROR)
    expect(error).to_be_visible()
    expect(error).to_have_text("Error: First Name is required")
    
def test_checkout_empty_last_name(authenticated_page: Page):
    """Test that checkout shows error when last name is empty"""
    add_item_to_cart(authenticated_page)
    navigate_to_checkout(authenticated_page)

    authenticated_page.fill(FIRST_NAME_INPUT, TEST_FIRST_NAME)
    authenticated_page.fill(ZIP_CODE_INPUT, TEST_ZIP_CODE)
    authenticated_page.click(CONTINUE_BUTTON)

    error = authenticated_page.locator(CHECKOUT_ERROR)
    expect(error).to_be_visible()
    expect(error).to_have_text("Error: Last Name is required")

def test_checkout_empty_zipcode(authenticated_page: Page):
    add_item_to_cart(authenticated_page)
    navigate_to_checkout(authenticated_page)

    authenticated_page.fill(FIRST_NAME_INPUT, TEST_FIRST_NAME)
    authenticated_page.fill(LAST_NAME_INPUT, TEST_LAST_NAME)
    authenticated_page.click(CONTINUE_BUTTON)

    error = authenticated_page.locator(CHECKOUT_ERROR)
    expect(error).to_be_visible()
    expect(error).to_have_text("Error: Postal Code is required")

def test_cancel_checkout(authenticated_page: Page):
    """Test that checkout shows error when first name is empty"""
    add_item_to_cart(authenticated_page)
    navigate_to_checkout(authenticated_page)

    authenticated_page.click(CANCEL_BUTTON)

    expect(authenticated_page).to_have_url(CART_URL)
    expect(authenticated_page.locator(CART_ITEM)).to_be_visible()