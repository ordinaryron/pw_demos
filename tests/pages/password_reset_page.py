from playwright.sync_api import Page

class PasswordResetPage:
    def __init__(self, page: Page):
        self.page = Page

        self.heading = page.get_by_role("heading", level=1)
        self.banner = page.locator("#confirmation-alert")