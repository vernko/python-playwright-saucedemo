"""
Tests for different user role behaviors.
Tests locked_out_user, problem_user, and performance_glitch_user.
"""

import pytest
from playwright.sync_api import Page, expect
from tests.helpers.constants import (
    LOGIN_URL,
    USERNAME_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    ERROR_MESSAGE,
    INVENTORY_TITLE,
    LOCKED_OUT_USER,
    STANDARD_PASSWORD,
)

def test_locked_out_user_cannot_login(page: Page):
    """Test that locked_out_user gets error message and cannot log in"""
    page.goto(LOGIN_URL)
    page.fill(USERNAME_INPUT, LOCKED_OUT_USER)
    page.fill(PASSWORD_INPUT, STANDARD_PASSWORD)
    page.click(LOGIN_BUTTON)
    expect(page.locator(ERROR_MESSAGE)).to_be_visible()
    expect(page.locator(ERROR_MESSAGE)).to_contain_text("Sorry, this user has been locked out.")
    expect(page).to_have_url(LOGIN_URL)

def test_problem_user_test(problem_user_page: Page):
    """Test that problem_user can log in and see inventory despite UI quirks"""
    # Just verify they got to the inventory page
    expect(problem_user_page.locator(INVENTORY_TITLE)).to_have_text("Products")
    # Note: This user has known issues with images, but login/access works

def test_performance_glitch_user_test(performance_glitch_user_page: Page):
    """Test that known ui issues work with performance_glitch_user"""
    # Just verify they got to the inventory page
    expect(performance_glitch_user_page.locator(INVENTORY_TITLE)).to_have_text("Products")
    # Note: This user has known issues with performance/loading, but login/access works