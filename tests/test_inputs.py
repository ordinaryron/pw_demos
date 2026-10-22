from playwright.sync_api import Page, sync_playwright, expect
from pages import InputsPage
import pytest

# Visits https://practice.expandtesting.com/inputs and tests the input fields.

meaningful_text = "Web inputs page for Automation Testing Practice"

def test_inputs(page: Page):
    inputs_page = InputsPage(page)
    
    # Load the page and check for a good response
    response = inputs_page.navigate()
    assert response.ok
    
    # For good measure, we'll also check for a meaningful heading.
    expect(inputs_page.heading).to_have_text(meaningful_text)
    
    # Let's make sure the input fields exist and the visibility buttons exist and are visible or not visible, as appropriate.
    expect(inputs_page.display_button).to_be_visible()
    expect(inputs_page.clear_button).to_be_visible()
    expect(inputs_page.input_number).to_be_visible() 
    expect(inputs_page.input_text).to_be_visible()
    expect(inputs_page.input_password).to_be_visible()
    expect(inputs_page.input_date).to_be_visible()
    expect(inputs_page.output_number).not_to_be_visible()
    expect(inputs_page.output_text).not_to_be_visible()
    expect(inputs_page.output_password).not_to_be_visible()
    expect(inputs_page.output_date).not_to_be_visible()

    # We'll put values in the input boxes:
    inputs_page.input_number.fill("8675309")
    inputs_page.input_text.fill("Interesting text here")
    inputs_page.input_password.fill("12345")
    inputs_page.input_date.fill("2025-12-31")

    # Click the display button to make the output fields visible.
    inputs_page.display_button.click()
    expect(inputs_page.output_number).to_be_visible()
    expect(inputs_page.output_text).to_be_visible()
    expect(inputs_page.output_password).to_be_visible()
    expect(inputs_page.output_date).to_be_visible()

    # The output fields should contain the values we gave the input fields. _to_have_value doesn't work here because these aren't input fields.
    expect(inputs_page.output_number).to_have_text("8675309")
    expect(inputs_page.output_text).to_have_text("Interesting text here")
    expect(inputs_page.output_password).to_have_text("12345")
    expect(inputs_page.output_date).to_have_text("2025-12-31")

    # The clear_inputs button both removes the values and sets the output fields back to not visible. We'll test that both events occur.
    inputs_page.clear_button.click()
    expect(inputs_page.input_number).to_have_value("")
    expect(inputs_page.input_text).to_have_value("")
    expect(inputs_page.input_password).to_have_value("")
    expect(inputs_page.input_date).to_have_value("")
    expect(inputs_page.output_number).not_to_be_visible()
    expect(inputs_page.output_text).not_to_be_visible()
    expect(inputs_page.output_password).not_to_be_visible()
    expect(inputs_page.output_date).not_to_be_visible()