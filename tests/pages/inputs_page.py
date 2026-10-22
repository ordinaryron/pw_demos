from playwright.sync_api import Page, Response

class InputsPage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        self.display_button = page.get_by_role("button", name="Display Inputs")
        self.clear_button = page.get_by_role("button", name="Clear Inputs")
        self.input_number = page.locator("#input-number")
        self.input_text = page.locator("#input-text")
        self.input_password = page.locator("#input-password")
        self.input_date = page.locator("#input-date")
        self.output_number = page.locator("#output-number")
        self.output_text = page.locator("#output-text")
        self.output_password = page.locator("#output-password")
        self.output_date = page.locator("#output-date")

    def navigate(self) -> Response:
        return self.page.goto("/inputs")

    def click_display_button(self):
        self.display_button.click()

    def click_clear_button(self):
        self.clear_button.click()