from playwright.sync_api import Page, sync_playwright, expect
from pages import LocatorsPage

meaningful_text = "Locators Test page for Automation Testing"

def test_locators(page: Page):
    locators_page = LocatorsPage(page)

    # Load the page and check for a good response
    response = locators_page.navigate()
    assert response.ok
            
    # For good measure, we'll also check for a meaningful heading.
    expect(locators_page.heading).to_have_text(meaningful_text)

    # This page provides various elements with the idea that each element is located via a different, specified method. We'll follow that via POM.
    # Not testing functionality too much here, mostly just making sure the elements are visible (meaning that they the locators are working as expected)
    expect(locators_page.add_item_button).to_be_visible()
    expect(locators_page.contact_link).to_be_visible()
    expect(locators_page.deal_text).to_be_visible()
    expect(locators_page.country_dropdown).to_be_visible()
    expect(locators_page.email_input).to_be_visible()
    expect(locators_page.search_input).to_be_visible()
    expect(locators_page.filter_input).to_be_visible()
    expect(locators_page.avatar_image).to_be_visible()
    expect(locators_page.reload_button).to_be_visible()
    expect(locators_page.settings_button).to_be_visible()
    expect(locators_page.systems_banner).to_be_visible()
    expect(locators_page.systems_banner).to_contain_text("All systems operational")
    expect(locators_page.username_text).to_be_visible()
    expect(locators_page.username_text).to_contain_text("Alice")
    expect(locators_page.legacy_css_target).to_be_visible()
    expect(locators_page.legacy_css_target).to_contain_text("This is a legacy CSS target")

    expect(locators_page.xpath_list).to_be_visible()
    expect(locators_page.xpath_list_option1).to_be_visible()
    expect(locators_page.xpath_list_option1).to_contain_text("Task 1: Review")
    expect(locators_page.xpath_list_option2).to_be_visible()
    expect(locators_page.xpath_list_option2).to_contain_text("Task 2: Implement")
    expect(locators_page.xpath_list_option3).to_be_visible()
    expect(locators_page.xpath_list_option3).to_contain_text("Task 3: Deploy")

    expect(locators_page.xpath_table).to_be_visible()
    expect(locators_page.xpath_table_header).to_be_visible()
    expect(locators_page.xpath_table_header_cell1).to_be_visible()
    expect(locators_page.xpath_table_header_cell1).to_contain_text("Product")
    expect(locators_page.xpath_table_header_cell2).to_be_visible()
    expect(locators_page.xpath_table_header_cell2).to_contain_text("Status")
    expect(locators_page.xpath_table_header_cell3).to_be_visible()
    expect(locators_page.xpath_table_header_cell3).to_contain_text("Stock")
    expect(locators_page.xpath_table_row1).to_be_visible()
    expect(locators_page.xpath_table_row1_cell1).to_be_visible()
    expect(locators_page.xpath_table_row1_cell1).to_contain_text("Headphones")
    expect(locators_page.xpath_table_row1_cell2).to_be_visible()
    expect(locators_page.xpath_table_row1_cell2).to_contain_text("Available")
    expect(locators_page.xpath_table_row1_cell3).to_be_visible()
    expect(locators_page.xpath_table_row1_cell3).to_contain_text("12")
    expect(locators_page.xpath_table_row2).to_be_visible()
    expect(locators_page.xpath_table_row2_cell1).to_be_visible()
    expect(locators_page.xpath_table_row2_cell1).to_contain_text("Monitor")
    expect(locators_page.xpath_table_row2_cell2).to_be_visible()
    expect(locators_page.xpath_table_row2_cell2).to_contain_text("Out of stock")
    expect(locators_page.xpath_table_row2_cell3).to_be_visible()
    expect(locators_page.xpath_table_row2_cell3).to_contain_text("0")
    expect(locators_page.xpath_table_row3).to_be_visible()
    expect(locators_page.xpath_table_row3_cell1).to_be_visible()
    expect(locators_page.xpath_table_row3_cell1).to_contain_text("Keyboard")
    expect(locators_page.xpath_table_row3_cell2).to_be_visible()
    expect(locators_page.xpath_table_row3_cell2).to_contain_text("Available")
    expect(locators_page.xpath_table_row3_cell3).to_be_visible()
    expect(locators_page.xpath_table_row3_cell3).to_contain_text("5")