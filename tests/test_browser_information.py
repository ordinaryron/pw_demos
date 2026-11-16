from playwright.sync_api import Page, sync_playwright, expect
from pages import BrowserInformationPage
import pytest

meaningful_text = "My Browser Information page for Automation Testing Practice"
show_text = "Show Browser Information"
hide_text = "Hide Browser Information"

@pytest.mark.parametrize("custom_page", ["chromium", "webkit"], indirect=True)
def test_browser_information(browser_information_page: BrowserInformationPage):

    # Load the page and check for a good response
    response = browser_information_page.navigate()
    assert response.ok

    # Verify the button is visible and the table is not visible; also verify that the button reads "Show Browser Information"
    expect(browser_information_page.heading).to_be_visible()
    expect(browser_information_page.heading).to_have_text(meaningful_text)
    expect(browser_information_page.toggle_button).to_be_visible()
    expect(browser_information_page.toggle_button).to_have_text(show_text)
    expect(browser_information_page.browser_table).not_to_be_visible()

    # Verify that when the button is clicked, the table is visible and the button text changes
    browser_information_page.toggle_browser_table()

    expect(browser_information_page.toggle_button).to_have_text(hide_text)
    expect(browser_information_page.browser_table).to_be_visible()

    browser_cell = browser_information_page.browser_table.locator("#browser-name")
    browser = browser_cell.inner_text()
    browser_type_name = browser_information_page.page.context.browser.browser_type.name
    if browser_type_name == "chromium":
        assert browser == "Google Chrome"
    elif browser_type_name == "webkit":
        assert browser == "Apple Safari"
    else:
        raise ValueError("Error: Browser value not found")