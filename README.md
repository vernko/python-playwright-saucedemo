# Python Playwright - SauceDemo Test Suite

Automated testing suite for SauceDemo e-commerce site using Python and Playwright, focusing on authentication flows and user role testing.

## Setup
```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Install Playwright browsers
uv run playwright install
```

## Run Tests
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_login.py -v

# Run in headed mode
uv run pytest --headed
```

## Project Structure
```
tests/
├── helpers/          # Helper functions and utilities
└── test_login.py    # Login functionality tests
```

## Technologies

- Python 3.x
- Playwright
- pytest