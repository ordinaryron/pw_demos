from playwright.sync_api import Page, Response

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

        self.error_banner = page.locator("#flash")
        self.heading = page.get_by_role("heading", level=1)
        self.username_label = page.get_by_text("Username", exact=True)
        self.password_label = page.get_by_text("Password", exact=True)
        self.confirm_password_label = page.get_by_text("Confirm Password", exact=True)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.confirm_password_input = page.locator("#confirmPassword")
        self.register_button = page.get_by_role("button", name="Register")

    def navigate(self) -> Response:
        return self.page.goto("/register")

    def register_account(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.register_button.click()