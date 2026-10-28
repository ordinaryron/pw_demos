from playwright.sync_api import Page, sync_playwright, expect
from pages import OneTimePasswordPage, OneTimePasswordVerificationPage, SecurePage
import re

meaningful_text = "OTP Login page for Automation Testing Practice"
meaningful_text_2 = "OTP Verification"
meaningful_text_3 = "Secure Area page for Automation Testing Practice"

def test_otp(page: Page, validate_invalid_emails):
    otp_page = OneTimePasswordPage(page)
    otp_verification_page = OneTimePasswordVerificationPage(page)
    secure_page = SecurePage(page)

    # Load the page and check for a good response
    response = otp_page.navigate()
    assert response.ok

    # For good measure, we'll also check for a meaningful heading.
    expect(otp_page.heading).to_have_text(meaningful_text)
    
    # Check all elements are visible (or not visible, as appropriate)
    expect(otp_page.heading).to_be_visible()
    expect(otp_page.email_label).to_be_visible()
    expect(otp_page.input_email).to_be_visible()
    expect(otp_page.submit_button).to_be_visible()
    expect(otp_page.error_message).not_to_be_visible()

    # Let's send a valid email address and make sure we end up in the right place.
    otp_page.send_otp_code()
    # We should be on the verification page, so let's confirm that. The URL remains the same so we have to check elements on the page.
    expect(otp_verification_page.heading).to_be_visible()
    expect(otp_verification_page.heading).to_have_text(meaningful_text_2)
    expect(otp_verification_page.alert).to_be_visible()
    expect(otp_verification_page.alert).to_contain_text("practice@expandtesting.com")
    expect(otp_verification_page.otp_input).to_be_visible()
    expect(otp_verification_page.otp_submit_button).to_be_visible()
    expect(otp_verification_page.error).not_to_be_visible()

    # Submitting the correct otp should take us to the secure login page. We can validate the url there, among other things.
    otp_verification_page.enter_valid_otp()
    expect(page).to_have_url(re.compile(r"/secure$"))
    expect(secure_page.heading).to_have_text(meaningful_text_3)
    expect(secure_page.greeting_text).to_contain_text("Hi, Guest")
    secure_page.logout()

    # Let's ensure the field only submits valid emails.
    otp_page.navigate()
    validate_invalid_emails(email_field=otp_page.input_email, submit_button=otp_page.submit_button, error_message=otp_page.error_message)

    # And then let's make sure the OTP code input behaves properly if entering a bad code, or no code at all. (Shame!)
    otp_page.navigate()
    otp_page.send_otp_code()
    bad_code = "000000"
    otp_verification_page.otp_input.fill(bad_code)
    otp_verification_page.otp_submit_button.click()
    expect(otp_verification_page.alert).to_contain_text("The provided OTP code is incorrect. Please check your code and try again.")
    expect(page).to_have_url(re.compile(r"/otp-verification$"))
    otp_verification_page.otp_submit_button.click()
    expect(otp_verification_page.error).to_be_visible()