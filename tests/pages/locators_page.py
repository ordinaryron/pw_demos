from playwright.sync_api import Page, Response

class LocatorsPage:
    def __init__(self, page: Page):
        self.page = page

        self.heading = page.get_by_role("heading", level=1)
        
        # Get by role
        self.add_item_button = page.get_by_role("Button", name="Add Item")
        self.contact_link = page.get_by_role("Link", name="Contact")

        # Get by text
        self.deal_text = page.get_by_text("Hot Deal: Buy 1 Get 1 Free")

        # Get by label
        self.country_dropdown = page.get_by_label("Choose a country")
        self.email_input = page.get_by_label("Email for newsletter")

        # Get by placeholder
        self.search_input = page.get_by_placeholder("Search the site")
        self.filter_input = page.get_by_placeholder("Filter by tag")

        # Get by alt text
        self.avatar_image = page.get_by_alt_text("User avatar")

        # Get by title
        self.reload_button = page.get_by_title("Refresh content")
        self.settings_button = page.get_by_title("Settings panel")

        # Get by test ID (yes please)
        self.systems_banner = page.get_by_test_id("status-message")
        self.username_text = page.get_by_test_id("user-name")

        # Get by legacy CSS
        self.legacy_css_target = page.locator(".legacy-css")

        # Get by XPath - List
        self.xpath_list = page.locator('//*[@id="core"]/div[1]/div/div/div[9]/ul')
        self.xpath_list_option1 = page.locator('//*[@id="core"]/div[1]/div/div/div[9]/ul/li[1]')
        self.xpath_list_option2 = page.locator('//*[@id="core"]/div[1]/div/div/div[9]/ul/li[2]')
        self.xpath_list_option3 = page.locator('//*[@id="core"]/div[1]/div/div/div[9]/ul/li[3]')

        # Get by XPath - Table
        self.xpath_table = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table')
        self.xpath_table_header = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/thead/tr')
        self.xpath_table_header_cell1 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/thead/tr/th[1]')
        self.xpath_table_header_cell2 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/thead/tr/th[2]')
        self.xpath_table_header_cell3 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/thead/tr/th[3]')
        self.xpath_table_row1 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[1]')
        self.xpath_table_row1_cell1 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[1]/td[1]')
        self.xpath_table_row1_cell2 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[1]/td[2]')
        self.xpath_table_row1_cell3 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[1]/td[3]')
        self.xpath_table_row2 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[2]')
        self.xpath_table_row2_cell1 =  page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[2]/td[1]')
        self.xpath_table_row2_cell2 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[2]/td[2]')
        self.xpath_table_row2_cell3 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[2]/td[3]')
        self.xpath_table_row3 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[3]')
        self.xpath_table_row3_cell1 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[3]/td[1]')
        self.xpath_table_row3_cell2 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[3]/td[2]')
        self.xpath_table_row3_cell3 = page.locator('//*[@id="core"]/div[1]/div/div/div[10]/table/tbody/tr[3]/td[3]')

    def navigate(self) -> Response:
        return self.page.goto("/locators")