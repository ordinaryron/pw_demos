from playwright.sync_api import Page, Response
import re, json

class PaginatedTablePage:
    def __init__(self, page: Page):
        self.page = page

        self.data_script = page.locator("script:has-text('let sheetData')")
        self.heading = page.get_by_role("heading", level=1)
        self.page_size_dropdown = page.locator("select[name='example_length']")
        self.page_size_dropdown_option = page.locator("select[name='example_length'] option")
        self.student_title_row = page.locator("table thead tr").filter(has_text="Student Name")
        self.student_table = page.locator("#demo")
        self.previous_button = page.locator("#example_previous")
        self.next_button = page.locator("a[data-dt-idx='next']")
        self.disabled_next_button = page.locator("[role='link'][aria-disabled='true']")
        self.search_input = page.get_by_label("Search")
        self.table_rows = page.locator("#example tbody tr")

    def navigate(self) -> Response:
        return self.page.goto("/dynamic-pagination-table")

    def get_all_dropdown_options(self) -> list[str]:
        dropdown_list = self.page_size_dropdown_option.all_text_contents()
        return dropdown_list

    def extract_sheet_data(self) -> json:
        # This function extracts the data from the Javascript on the page and returns it as json
        raw_js = self.page.evaluate("""() => {
            const scripts = Array.from(document.querySelectorAll('script'));
            const targetScript = scripts.find(s => s.textContent.includes('let sheetData'));
            return targetScript ? targetScript.textContent : '';
        }""")
        if not raw_js:
            raise ValueError("Could not locate a <script> block contaning 'sheetData'")
        match = re.search(r"sheetData\s*=\s*(\[.*?\]);", raw_js, re.DOTALL)
        if match:
            raw_json_string = match.group(1)
            fixed_json_string = re.sub(r'([\w_]+)\s*:', r'"\1":', raw_json_string)
            return json.loads(fixed_json_string)
        raise ValueError("Found the script block but could not parse the 'sheetData' array")

    def execute_search(self, search_term) -> list[str]:
        self.search_input.fill(search_term)
        rows = self.table_rows.all_inner_texts()
        all_rows = []
        all_rows += rows
        aria_is_disabled = self.next_button.get_attribute("aria-disabled") == "true"
        if aria_is_disabled:
            pass
        else:
            self.next_button.click()
            rows = self.table_rows.all_inner_texts()
            all_rows += rows
        if any("No matching records found" in row for row in all_rows):
            return []
        else:
            return all_rows