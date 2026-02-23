# Python Playwright - SauceDemo E-Commerce Test Suite

[![Playwright Tests](https://github.com/vernko/python-playwright-saucedemo/actions/workflows/playwright.yml/badge.svg)](https://github.com/vernko/python-playwright-saucedemo/actions/workflows/playwright.yml)

Comprehensive end-to-end UI test automation suite for the SauceDemo e-commerce application using Python and Playwright. Demonstrates production-ready test automation practices including authentication flows, shopping cart operations, checkout validation, and multi-user role testing with CI/CD integration.

## Features

- ✅ **Complete E-Commerce Flow Testing** - Login → Browse → Add to Cart → Checkout → Order Complete
- ✅ **Multi-User Role Testing** - Standard, Locked Out, Problem User, Performance Glitch User scenarios
- ✅ **Form Validation Testing** - Negative test cases for checkout field validation
- ✅ **Cross-Browser Testing** - Automated tests across Chromium, Firefox, and WebKit
- ✅ **Reusable Test Fixtures** - Pre-authenticated user sessions for efficient testing
- ✅ **Helper Functions** - Modular, maintainable test utilities
- ✅ **CI/CD Integration** - Automated test execution via GitHub Actions
- ✅ **Centralized Configuration** - Constants file for easy maintenance

## Tech Stack

- **Language:** Python 3.12
- **Automation Framework:** Playwright
- **Test Framework:** pytest
- **CI/CD:** GitHub Actions
- **Package Manager:** uv

## Project Structure
```
python-playwright-saucedemo/
├── tests/
│   ├── helpers/
│   │   ├── constants.py      # URLs, selectors, test data
│   │   ├── fixtures.py       # Reusable authenticated user sessions
│   │   └── helpers.py        # Common test operations (cart, checkout)
│   ├── conftest.py           # Pytest configuration
│   ├── test_login.py         # Authentication and login validation
│   ├── test_cart.py          # Shopping cart operations
│   ├── test_checkout.py      # Checkout flow and form validation
│   ├── test_inventory.py    # Product display and inventory page
│   └── test_user_roles.py   # Different user role behaviors
├── .github/
│   └── workflows/
│       └── playwright.yml    # CI/CD configuration
├── pyproject.toml            # Project dependencies
├── pytest.ini                # Pytest configuration
└── README.md
```

## Test Coverage

### Authentication & User Roles (`test_login.py`, `test_user_roles.py`)
- ✅ Valid user login
- ✅ Invalid credentials error handling
- ✅ Locked out user validation
- ✅ Problem user login (UI quirks)
- ✅ Performance glitch user login (slow loading)

### Shopping Cart (`test_cart.py`)
- ✅ Add single item to cart
- ✅ Add multiple items to cart
- ✅ Remove item from cart
- ✅ Cart badge count updates
- ✅ Cart state persistence

### Checkout Flow (`test_checkout.py`)
- ✅ Complete end-to-end checkout
- ✅ First name validation (required field)
- ✅ Last name validation (required field)
- ✅ Zip code validation (required field)
- ✅ Checkout cancellation
- ✅ Order completion confirmation

### Inventory (`test_inventory.py`)
- ✅ Product page loads for authenticated users
- ✅ Products display correctly
- ✅ Different user roles can access inventory

## Setup

### Prerequisites
- Python 3.12+
- uv package manager

### Installation
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/vernko/python-playwright-saucedemo.git
cd python-playwright-saucedemo

# Install dependencies
uv sync

# Install Playwright browsers
uv run playwright install
```

## Running Tests
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_login.py -v

# Run specific test
uv run pytest tests/test_checkout.py::test_complete_checkout -v

# Run in headed mode (see browser)
uv run pytest --headed

# Run with HTML report
uv run pytest --html=report.html

# Run specific browser
uv run pytest --browser firefox
```

## Key Design Patterns

### Reusable Fixtures
Pre-authenticated user sessions for efficient test execution:
```python
def test_add_to_cart(authenticated_page: Page):
    # Page already logged in as standard_user
    add_item_to_cart(authenticated_page)
```

### Centralized Configuration
All URLs, selectors, and test data in `constants.py` for easy maintenance:
```python
from tests.helpers.constants import LOGIN_URL, STANDARD_USER
```

### Helper Functions
Reusable operations for common workflows:
```python
from tests.helpers.helpers import add_item_to_cart, navigate_to_checkout
```

## CI/CD Pipeline

Tests run automatically on GitHub Actions for:
- Every push to `main` branch
- Every pull request to `main` branch

**Pipeline includes:**
- Setup Python 3.12 environment
- Install dependencies with uv
- Install Playwright browsers
- Execute full test suite across Chromium, Firefox, WebKit
- Generate test reports

View test results in the [Actions tab](https://github.com/vernko/python-playwright-saucedemo/actions).

## Key Testing Concepts Demonstrated

- **End-to-End Testing** - Complete user flows from login to order completion
- **Negative Testing** - Form validation and error handling
- **Multi-User Testing** - Different user roles and behaviors
- **Test Fixtures** - Reusable test setup and teardown
- **Cross-Browser Testing** - Multi-browser compatibility validation
- **CI/CD Integration** - Automated testing in deployment pipeline
- **Maintainable Architecture** - Helper functions, constants, and modular design

## Test Execution Results

All tests pass consistently across:
- ✅ Chromium
- ✅ Firefox
- ✅ WebKit

Tests cover **5 major functional areas** with **20+ test cases**.