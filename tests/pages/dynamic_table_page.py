from playwright.sync_api import Page, Response

class DynamicTablePage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        self.title_row = page.locator("table thead tr").filter(has_text="Name")
        self.firefox_row = page.locator("table tbody tr").filter(has_text="Firefox")
        self.chrome_row = page.locator("table tbody tr").filter(has_text="Chrome")
        self.internet_explorer_row = page.locator("table tbody tr").filter(has_text="Internet Explorer")
        self.system_row = page.locator("table tbody tr").filter(has_text="System")
        self.target_row = page.locator("#chrome-cpu")

    def navigate(self) -> Response:
        return self.page.goto("/dynamic-table")