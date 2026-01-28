import pytest
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    """Test login with valid credentials"""
    page.goto("https://www.saucedemo.com/")

    # Fill login form
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # Verify we're on the products page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

def test_invalid_login(page: Page):
    """Test login with invalid credentials"""
    page.goto("https://www.saucedemo.com/")
    
    page.fill("#user-name", "invalid_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    
    # Verify error message appears
    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")