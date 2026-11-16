import pytest
from playwright.sync_api import Page, Playwright, Locator, expect
from typing import Callable
from collections.abc import Generator
from pages.browser_information_page import BrowserInformationPage

@pytest.fixture
def validate_invalid_emails(page: Page) -> Callable[[Locator, Locator, Locator], None]:
    def _validate(email_field: Locator, submit_button: Locator, error_message: Locator):
        bad_addresses = ["noatsymbol", "too@many@at@symbols"]
        for bad_address in bad_addresses:
            email_field.fill(bad_address)
            submit_button.click()
            expect(error_message).to_be_visible()
    return _validate

@pytest.fixture
def custom_page(playwright: Playwright, request, browser_type_launch_args: dict, browser_context_args: dict) -> Generator[Page, None, None]:
    browser_type = getattr(request, "param", "chromium")
    browser = getattr(playwright, browser_type).launch(**browser_type_launch_args)
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture
def browser_information_page(custom_page: Page) -> BrowserInformationPage:
    return BrowserInformationPage(custom_page)