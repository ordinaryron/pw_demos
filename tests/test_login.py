from playwright.sync_api import Page, sync_playwright, expect
from pages import LoginPage, SecurePage
from dotenv import load_dotenv
import re, os

# Visits https://practice.expandtesting.com/login and tests login functionality.

meaningful_text = "Test Login page for Automation Testing Practice"
meaningful_text_2 = "Secure Area page for Automation Testing Practice"

load_dotenv()

def test_login(page: Page):
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    # Load the page and check for a good response
    response = login_page.navigate()
    assert response.ok
        
    # For good measure, we'll also check for a meaningful heading.
    expect(login_page.heading).to_have_text(meaningful_text)

    # Check all elements are visible (or not visible, as appropriate)
    expect(login_page.secure_alert_banner).not_to_be_visible()
    expect(login_page.username_label).to_be_visible()
    expect(login_page.password_label).to_be_visible()
    expect(login_page.input_username).to_be_visible()
    expect(login_page.input_password).to_be_visible()
    expect(login_page.login_button).to_be_visible()
    expect(login_page.bad_username_password_banner).not_to_be_visible()

    # Login using the control on the page. (POM)
    login_page.login_good_credentials()

    expect(page).to_have_url(re.compile(r"/secure$"))

    # Have we logged in, though? There are specific elements on the login page we should see.
    expect(secure_page.secure_alert_banner).to_be_visible()
    expect(secure_page.greeting_text).to_be_visible()
    expect(secure_page.greeting_text).to_contain_text(os.getenv("TEST_USERNAME"))
    expect(secure_page.heading).to_be_visible()
    expect(secure_page.heading).to_have_text(meaningful_text_2)
    expect(secure_page.secure_text).to_be_visible()
    expect(secure_page.logout_button).to_be_visible()

    # Let's logout and make sure we see the login page and correct banner.
    secure_page.logout_button.click()

    expect(page).to_have_url(re.compile(r"/login$"))
    expect(login_page.secure_alert_banner).to_be_visible
    expect(login_page.username_label).to_be_visible()
    expect(login_page.password_label).to_be_visible()
    expect(login_page.input_username).to_be_visible()
    expect(login_page.input_password).to_be_visible()
    expect(login_page.login_button).to_be_visible()

    # Finally, let's make sure we get the "bad username" and "bad password" errors when logging in with
    # bad usernames and bad passwords
    page.reload()
    login_page.login_bad_username()
    expect(page).to_have_url(re.compile(r"/login$")) # We do not reach the secure page
    expect(login_page.bad_username_password_banner).to_be_visible()
    expect(login_page.bad_username_password_banner).to_contain_text("Your username is invalid!")

    page.reload()
    login_page.login_bad_password()
    expect(page).to_have_url(re.compile(r"/login$"))
    expect(login_page.bad_username_password_banner).to_be_visible()
    expect(login_page.bad_username_password_banner).to_contain_text("Your password is invalid!")