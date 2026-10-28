from playwright.sync_api import Page, sync_playwright, expect
from pages import RegisterPage, LoginPage, SecurePage
import re, time

# Visits https://practice.expandtesting.com/register and tests registration functionality.

meaningful_text = "Test Register page for Automation Testing Practice"
test_username = "ron-885"
test_password = "test_password"

def test_register(page: Page):
    register_page = RegisterPage(page)
    login_page = LoginPage(page)
    secure_page = SecurePage(page)

    # Load the page and check for a good response
    response = register_page.navigate()
    assert response.ok
        
    # For good measure, we'll also check for a meaningful heading.
    expect(register_page.heading).to_have_text(meaningful_text)

    # Check all elements are visible (or not visible, as appropriate)
    expect(register_page.error_banner).not_to_be_visible()
    expect(register_page.heading).to_be_visible()
    expect(register_page.heading).to_have_text(meaningful_text)
    expect(register_page.username_label).to_be_visible()
    expect(register_page.password_label).to_be_visible()
    expect(register_page.confirm_password_label).to_be_visible()
    expect(register_page.username_input).to_be_visible()
    expect(register_page.password_input).to_be_visible()
    expect(register_page.confirm_password_input).to_be_visible()
    expect(register_page.register_button).to_be_visible()

    # After filling the username, password, and confirm_password fields and clicking the Register button, we are taken to the 
    # login page with a banner indicating successful registration. We'll then login using the new username and password to 
    # confirm registration.

    register_page.register_account(test_username, test_password)
    expect(page).to_have_url(re.compile(r"/login$"))
    expect(login_page.bad_username_password_banner).to_contain_text("Successfully registered, you can log in now.")
    login_page.login_arbitrary_credentials(test_username, test_password)
    expect(page).to_have_url(re.compile(r"/secure$"))
    expect(secure_page.secure_alert_banner).to_be_visible()
    expect(secure_page.greeting_text).to_be_visible()
    expect(secure_page.greeting_text).to_contain_text(test_username)
    secure_page.logout_button.click()

    # Return to the registration page and try registering with the same username and password. The error banner should be visible
    # and we do not end up on the login page.
    register_page.navigate()
    register_page.register_account(test_username, test_password)
    expect(page).to_have_url(re.compile(r"/register$"))
    expect(register_page.error_banner).to_be_visible()
    expect(register_page.error_banner).to_have_text("An error occurred during registration. Please try again.")

    # Let's try some various negtative testing scenarios.

    # Clicking the Register button without filling in any text fields.
    register_page.navigate()
    register_page.register_button.click()
    expect(register_page.error_banner).to_be_visible()
    expect(register_page.error_banner).to_have_text("All fields are required.")


    # Clicking the Register button if we've only entered the username or password
    register_page.navigate()
    register_page.username_input.fill(test_username)
    register_page.register_button.click()
    expect(page).to_have_url(re.compile(r"/register$"))
    expect(register_page.error_banner).to_be_visible()
    expect(register_page.error_banner).to_have_text("All fields are required.")

    register_page.navigate()
    register_page.password_input.fill(test_password)
    register_page.register_button.click()
    expect(page).to_have_url(re.compile(r"/register$"))
    expect(register_page.error_banner).to_be_visible()
    expect(register_page.error_banner).to_have_text("All fields are required.")

    register_page.navigate()
    register_page.confirm_password_input.fill(test_password)
    register_page.register_button.click()
    expect(page).to_have_url(re.compile(r"/register$"))
    expect(register_page.error_banner).to_be_visible()
    expect(register_page.error_banner).to_have_text("All fields are required.")

    # The username must be:
    # --between 3 and 39 characters
    # --lowercase only
    # --no underscores or other special characters
    # --cannot start or end with a hyphen
    short_username_list = ["r", "ro"]
    bad_username_list = ["ron_123", "ronronronnooneneedsausernamethislongronronron", "r@n-123", "r#n-123", "r$n-123", "r%n-123", "r^n-123", "r&n-123", "r*n-123", "-on-123", "ron-12-"]
    for short_username in short_username_list:
        register_page.navigate()
        register_page.register_account(short_username, test_password)
        expect(page).to_have_url(re.compile(r"/register$"))
        expect(register_page.error_banner).to_be_visible()
        expect(register_page.error_banner).to_have_text("Username must be at least 3 characters long.")

    for bad_username in bad_username_list:
        register_page.navigate()
        register_page.register_account(bad_username, test_password)
        expect(page).to_have_url(re.compile(r"/register$"))
        expect(register_page.error_banner).to_be_visible()
        expect(register_page.error_banner).to_have_text("Invalid username. Usernames can only contain lowercase letters, numbers, and single hyphens, must be between 3 and 39 characters, and cannot start or end with a hyphen.")

    # Finally, we'll check the scenario where the password field and password confirmation field doesn't match
    bad_password = "test_password2"
    register_page.navigate()
    register_page.username_input.fill(test_username)
    register_page.password_input.fill(test_password)
    register_page.confirm_password_input.fill(bad_password)
    register_page.register_button.click()
    expect(page).to_have_url(re.compile(r"/register$"))
    expect(register_page.error_banner).to_be_visible()
    expect(register_page.error_banner).to_have_text("Passwords do not match.")