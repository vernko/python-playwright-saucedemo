"""
Tests for login flow.
Tests valid and invalid login.
"""

from playwright.sync_api import Page, expect
from tests.helpers.constants import (
    LOGIN_URL,
    INVENTORY_URL,
    USERNAME_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    ERROR_MESSAGE,
    INVENTORY_TITLE,
    STANDARD_USER,
    STANDARD_PASSWORD,
)

def test_valid_login(page: Page):
    """Test login with valid credentials"""
    page.goto(LOGIN_URL)

    # Fill login form
    page.fill(USERNAME_INPUT, STANDARD_USER)
    page.fill(PASSWORD_INPUT, STANDARD_PASSWORD)
    page.click(LOGIN_BUTTON)
    
    # Verify we're on the products page
    expect(page).to_have_url(INVENTORY_URL)
    expect(page.locator(INVENTORY_TITLE)).to_have_text("Products")

def test_invalid_login(page: Page):
    """Test login with invalid credentials"""
    page.goto(LOGIN_URL)
    
    page.fill(USERNAME_INPUT, "invalid_user")
    page.fill(PASSWORD_INPUT, "wrong_password")
    page.click(LOGIN_BUTTON)
    
    # Verify error message appears
    error = page.locator(ERROR_MESSAGE)
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")