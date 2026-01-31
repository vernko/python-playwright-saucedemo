import pytest
from playwright.sync_api import Page, expect
from tests.helpers.constants import (INVENTORY_TITLE, PRODUCT_ITEM)

def test_inventory_page_loads(authenticated_page: Page):
    """Test that we can see the inventory page when logged in"""
    expect(authenticated_page.locator(INVENTORY_TITLE)).to_have_text("Products")

def test_products_are_displayed(authenticated_page: Page):
    """Test that products show up on inventory page"""
    expect(authenticated_page.locator(PRODUCT_ITEM).first).to_be_visible()

def test_problem_user_can_login(problem_user_page: Page):
    """Test that a problem_user fixture logs in successfully"""
    expect(problem_user_page.locator(INVENTORY_TITLE).first).to_have_text("Products")

def test_performance_glitch_user_can_login(performance_glitch_user_page: Page):
    """Test that a problem_user fixture logs in successfully"""
    expect(performance_glitch_user_page.locator(INVENTORY_TITLE).first).to_have_text("Products")