from playwright.sync_api import Page, Response

class RadioButtonsPage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        self.color_label = page.get_by_text("Select your favorite color:")
        self.sport_label = page.get_by_text("Select your favorite sport:")
        self.radio_blue = page.get_by_role("radio", name="Blue", exact=True)
        self.radio_red = page.get_by_role("radio", name="Red", exact=True)
        self.radio_yellow = page.get_by_role("radio", name="Yellow", exact=True)
        self.radio_black = page.get_by_role("radio", name="Black", exact=True)
        self.radio_green = page.get_by_role("radio", name="Green", exact=True)
        self.radio_basketball = page.get_by_role("radio", name="Basketball", exact=True)
        self.radio_football = page.get_by_role("radio", name="Football", exact=True)
        self.radio_tennis = page.get_by_role("radio", name="Tennis", exact=True)

    def navigate(self) -> Response:
        return self.page.goto("/radio-buttons")

    def check_button(self, label: str):
        match label:
            case "Blue":
                self.radio_blue.check()
            case "Red":
                self.radio_red.check()
            case "Yellow":
                self.radio_yellow.check()
            case "Black":
                self.radio_black.check()
            case "Green":
                self.radio_green.check()
            case "Basketball":
                self.radio_basketball.check()
            case "Football":
                self.radio_football.check()
            case "Tennis":
                self.radio_tennis.check()
            case _:
                raise ValueError("Error: Invalid selection")