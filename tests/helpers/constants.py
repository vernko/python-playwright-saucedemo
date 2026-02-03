"""
Constants for SauceDemo test automation.
Contains URLs, selectors, and test user credentials.
"""

# Base URL
BASE_URL = "https://www.saucedemo.com"

# Page URLs
LOGIN_URL = f"{BASE_URL}/"
INVENTORY_URL = f"{BASE_URL}/inventory.html"
CART_URL = f"{BASE_URL}/cart.html"
CHECKOUT_STEP_ONE_URL = f"{BASE_URL}/checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = f"{BASE_URL}/checkout-step-two.html"
CHECKOUT_COMPLETE_URL = f"{BASE_URL}/checkout-complete.html"

# Selectors - Login
USERNAME_INPUT = "#user-name"
PASSWORD_INPUT = "#password"
LOGIN_BUTTON = "#login-button"
ERROR_MESSAGE = "[data-test='error']"

# Selectors - Inventory
INVENTORY_TITLE = ".title"
PRODUCT_ITEM = ".inventory_item"
CART_BADGE = ".shopping_cart_badge"

# Selectors - Cart
CART_ITEM = ".cart_item"
CHECKOUT_BUTTON = "#checkout"
CONTINUE_SHOPPING = "#continue-shopping"
REMOVE_BUTTON = "[data-test^='remove']"
ADD_TO_CART_BUTTON = "[data-test^='add-to-cart']"
CART_LINK = ".shopping_cart_link"

# Selectors - Checkout (add to your existing selectors)
FIRST_NAME_INPUT = "[data-test='firstName']"
LAST_NAME_INPUT = "[data-test='lastName']"
ZIP_CODE_INPUT = "[data-test='postalCode']"
CONTINUE_BUTTON = "[data-test='continue']"
FINISH_BUTTON = "[data-test='finish']"
CANCEL_BUTTON = "[data-test='cancel']"
CHECKOUT_COMPLETE_HEADER = ".complete-header"
CHECKOUT_ERROR = "[data-test='error']"

# Test Users
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"
LOCKED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PERFORMANCE_GLITCH_USER = "performance_glitch_user"

# Test checkout data
TEST_FIRST_NAME = "John"
TEST_LAST_NAME = "Doe"
TEST_ZIP_CODE = "12345"