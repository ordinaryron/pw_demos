from playwright.sync_api import Page, sync_playwright, expect
from pages import DynamicTablePage
import math

meaningful_text = "Dynamic Table page for Automation Testing Practice"

def test_dynamic_table(page: Page):
    dynamic_table_page = DynamicTablePage(page)

    # Load the page and check for a good response
    response = dynamic_table_page.navigate()
    assert response.ok
        
    # For good measure, we'll also check for a meaningful heading.
    expect(dynamic_table_page.heading).to_have_text(meaningful_text)

    # Make sure all the elements exist
    expect(dynamic_table_page.heading).to_be_visible()
    expect(dynamic_table_page.title_row).to_be_visible()
    expect(dynamic_table_page.chrome_row).to_be_visible()
    expect(dynamic_table_page.firefox_row).to_be_visible()
    expect(dynamic_table_page.internet_explorer_row).to_be_visible()
    expect(dynamic_table_page.system_row).to_be_visible()
    expect(dynamic_table_page.target_row).to_be_visible()

    # The idea is to confirm that the Chrome CPU load is the same as that in the target row. But, the table cells move around.
    # Here's how we'll tackle this:
    
    # 1. Use the title row to determine which column the CPU is
    title_values = dynamic_table_page.title_row.locator("th").all_text_contents()
    column = title_values.index('CPU')
    
    # 2. Extract the value in that column for the "Chrome" row.
    chrome_row_values = dynamic_table_page.chrome_row.locator("td").all_text_contents()
    chrome_cpu_value = chrome_row_values[column]
    # We'll remove everything from the % onward. This site appends text to the value for some reason, so this will strip it down to just the number.
    chrome_cpu_value_clean = float(chrome_cpu_value.split('%')[0])
    
    # 3. Compare to the value in the target row.
    target_cpu_value = dynamic_table_page.target_row.inner_text().removeprefix("Chrome CPU: ")
    target_cpu_value_clean = float(target_cpu_value.split('%')[0])

    # And finally, confirm that the two values are identical.
    assert chrome_cpu_value_clean == target_cpu_value_clean