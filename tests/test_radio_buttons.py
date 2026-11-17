from playwright.sync_api import Page, sync_playwright, expect
from pages import RadioButtonsPage

meaningful_text = "Radio Buttons page for Automation Testing Practice"



def test_radio_buttons(page: Page):
    radio_buttons_page = RadioButtonsPage(page)

    # Load the page and check for a good response
    response = radio_buttons_page.navigate()
    assert response.ok
            
    # For good measure, we'll also check for a meaningful heading.
    expect(radio_buttons_page.heading).to_have_text(meaningful_text)

    # Let's make sure all elements are visible
    expect(radio_buttons_page.color_label).to_be_visible()
    expect(radio_buttons_page.sport_label).to_be_visible()
    expect(radio_buttons_page.radio_blue).to_be_visible()
    expect(radio_buttons_page.radio_red).to_be_visible()
    expect(radio_buttons_page.radio_yellow).to_be_visible()
    expect(radio_buttons_page.radio_black).to_be_visible()
    expect(radio_buttons_page.radio_green).not_to_be_visible() # Green is disabled
    expect(radio_buttons_page.radio_basketball).to_be_visible()
    expect(radio_buttons_page.radio_football).to_be_visible()
    expect(radio_buttons_page.radio_tennis).to_be_visible()

    # Check the button nad make sure it is checked while others are not
    color_options = (
        (radio_buttons_page.radio_blue, "Blue"),
        (radio_buttons_page.radio_red, "Red"),
        (radio_buttons_page.radio_yellow, "Yellow"),
        (radio_buttons_page.radio_black, "Black"),
    )
    buttons_only = []
    for button, color in color_options:
        buttons_only.append(button)
    for button, color in color_options:
        radio_buttons_page.check_button(color)
        expect(button).to_be_checked()
        for butt in buttons_only:
            if butt == button:
                expect(butt).to_be_checked()
            else:
                expect(butt).not_to_be_checked()

    sport_options = (
        (radio_buttons_page.radio_basketball, "Basketball"),
        (radio_buttons_page.radio_football, "Football"),
        (radio_buttons_page.radio_tennis, "Tennis"),
    )

    buttons_only = []
    for button, sport in sport_options:
        buttons_only.append(button)
    for button, sport in sport_options:
        radio_buttons_page.check_button(sport)
        expect(button).to_be_checked()
        for butt in buttons_only:
            if butt == button:
                expect(butt).to_be_checked()
            else:
                expect(butt).not_to_be_checked()