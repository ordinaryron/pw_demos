from playwright.sync_api import Page

class OneTimePasswordVerificationPage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        self.alert = page.locator("#otp-message")
        self.otp_input = page.locator("#otp")
        self.otp_submit_button = page.get_by_role("button", name="Verify OTP Code")
        self.error = page.get_by_text("Please enter a correct 6-digit OTP code.")

    def enter_valid_otp(self):
        valid_otp = "214365"
        self.otp_input.fill(valid_otp)
        self.otp_submit_button.click()