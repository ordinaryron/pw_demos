from playwright.sync_api import Page, sync_playwright, expect
from pages import ForgotPasswordPage, PasswordResetPage

# Visits https://practice.expandtesting.com/inputs and tests the input fields.

meaningful_text = "Dummy Forgot Password form page for Automation Testing Practice"
meaningful_text_2 = "Password reset page for Automation Testing Practice"

def test_inputs(page: Page):
    forgotten_password_page = ForgotPasswordPage(page)
    password_reset_page = PasswordResetPage(page)
    
    # Load the page and check for a good response
    response = forgotten_password_page.navigate()
    assert response.ok
    
    # For good measure, we'll also check for a meaningful heading.
    expect(forgotten_password_page.heading).to_have_text(meaningful_text)

    # Let's make sure the input fields exist and the visibility buttons exist and are visible or not visible, as appropriate.
    expect(forgotten_password_page.heading).to_be_visible()
    expect(forgotten_password_page.email_label).to_be_visible()
    expect(forgotten_password_page.email_input).to_be_visible()
    expect(forgotten_password_page.email_button).to_be_visible()
    expect(forgotten_password_page.error_text).not_to_be_visible()

    # Submit the email and make sure we get the flash banner.
    forgotten_password_page.submit_email()

    expect(password_reset_page.banner).to_be_visible()
    expect(password_reset_page.banner).to_have_text("An e-mail has been sent to you which explains how to reset your password.")

    # A couple negative scenarios we can check. There isn't much input validation, but it does check to see if one and only @ is present in the email address, so we'll verify that.
    bad_addresses = ["noatsymbol", "too@many@at@symbols"]
    for bad_address in bad_addresses:
        forgotten_password_page.navigate()
        forgotten_password_page.email_input.fill(bad_address)
        forgotten_password_page.email_button.click()
        expect(forgotten_password_page.error_text).to_be_visible()