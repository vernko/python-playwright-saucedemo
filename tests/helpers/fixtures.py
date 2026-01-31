"""
Pytest fixtures for authenticated user sessions.
These fixtures automatically log in users before tests run.
"""

import pytest
from playwright.sync_api import Page, expect
from tests.helpers.constants import (
    LOGIN_URL,
    INVENTORY_URL,
    USERNAME_INPUT,
    PASSWORD_INPUT,
    LOGIN_BUTTON,
    INVENTORY_TITLE,
    STANDARD_USER,
    STANDARD_PASSWORD,
    PROBLEM_USER,
    PERFORMANCE_GLITCH_USER,
)

@pytest.fixture
def authenticated_page(page: Page) -> Page:
    """
    Fixture that provides a page with standard_user already logged in.

    Usage:
        def test_something(authenticated_page):
            # Page is already on inventory page, loggin in
            authenticated_page.locator(".some-element").click()

        Yields:
            Page: Playwright page object on the inventory page, authenticated
    """
    page.goto(LOGIN_URL)
    page.fill(USERNAME_INPUT, STANDARD_USER)
    page.fill(PASSWORD_INPUT, STANDARD_PASSWORD)
    page.click(LOGIN_BUTTON)

    expect(page).to_have_url(INVENTORY_URL)
    expect(page.locator(INVENTORY_TITLE)).to_have_text("Products")

    yield page

@pytest.fixture
def problem_user_page(page: Page) -> Page:
    """
    Fixture that provides a page with a problem_user (potential broken images & wrong products) logged in.

    Usage:
        def test_something(problem_user_page):
            # Page is already on inventory page, logged in
            problem_user_page.locator(".some-element").click()

        Yields:
            Page: Playwright page object on the inventory page, authenticated
    """
    page.goto(LOGIN_URL)
    page.fill(USERNAME_INPUT, PROBLEM_USER)
    page.fill(PASSWORD_INPUT, STANDARD_PASSWORD)
    page.click(LOGIN_BUTTON)

    expect(page).to_have_url(INVENTORY_URL)
    expect(page.locator(INVENTORY_TITLE)).to_have_text("Products")

    yield page

@pytest.fixture
def performance_glitch_user_page(page: Page) -> Page:
    """
    Fixture that provides a page with a performance_glitch_user (intentionally slow) logged in.

    Usage:
        def test_something(performance_glitch_user_page):
            # Page is already on inventory page, logged in
            performance_glitch_user_page.locator(".some-element").click()

        Yields:
            Page: Playwright page object on the inventory page, authenticated
    """
    page.goto(LOGIN_URL)
    page.fill(USERNAME_INPUT, PERFORMANCE_GLITCH_USER)
    page.fill(PASSWORD_INPUT, STANDARD_PASSWORD)
    page.click(LOGIN_BUTTON)

    expect(page).to_have_url(INVENTORY_URL, timeout=10000)
    expect(page.locator(INVENTORY_TITLE)).to_have_text("Products")

    yield page