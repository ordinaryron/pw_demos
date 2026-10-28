import pytest
from playwright.sync_api import Page, Locator, expect
from typing import Callable

@pytest.fixture
def validate_invalid_emails(page: Page) -> Callable[[Locator, Locator, Locator], None]:
    def _validate(email_field: Locator, submit_button: Locator, error_message: Locator):
        bad_addresses = ["noatsymbol", "too@many@at@symbols"]
        for bad_address in bad_addresses:
            email_field.fill(bad_address)
            submit_button.click()
            expect(error_message).to_be_visible()
    return _validate