from playwright.sync_api import Page, Response

class BrowserInformationPage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)

        # We have a button that reads "Show Browser Information" when the information is hidden, and "Hide Browser Information" when it is shown. 
        self.toggle_button = page.locator("#browser-toggle")
        self.browser_table = page.locator("#browser-info > table")

    def navigate(self) -> Response:
        return self.page.goto("/my-browser")

    def toggle_browser_table(self):
        self.toggle_button.click()