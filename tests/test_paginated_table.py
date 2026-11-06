from playwright.sync_api import Page, sync_playwright, expect
from pages import PaginatedTablePage
import pytest, time

meaningful_text = "Dynamic pagination Table page for Automation Testing Practice"

def test_paginated_table(page: Page):
    paginated_table_page = PaginatedTablePage(page)
    
    response = paginated_table_page.navigate()
    assert response.ok
            
    # For good measure, we'll also check for a meaningful heading.
    expect(paginated_table_page.heading).to_have_text(meaningful_text)

    # Check all elements are visible (or not visible, as appropriate)
    expect(paginated_table_page.heading).to_be_visible()
    expect(paginated_table_page.page_size_dropdown).to_be_visible()
    expect(paginated_table_page.student_title_row).to_be_visible()
    expect(paginated_table_page.student_table).to_be_visible()
    expect(paginated_table_page.previous_button).to_be_visible()
    expect(paginated_table_page.next_button).to_be_visible()
    expect(paginated_table_page.disabled_next_button).not_to_be_visible()
    expect(paginated_table_page.search_input).to_be_visible()
    assert paginated_table_page.page_size_dropdown.input_value() == "3"

    # For good measure, we'll make sure "Previous" is disabled by default and "Next" is enabled by default
    expect(paginated_table_page.previous_button).to_have_class("paginate_button page-item previous disabled")
    expect(paginated_table_page.next_button).to_be_enabled()

    # How may options are there in the drop down, and what are they?
    option_list = paginated_table_page.get_all_dropdown_options()
    option_count = paginated_table_page.page_size_dropdown.count()

    # Let's get all the data.
    sheet_data = paginated_table_page.extract_sheet_data()
    num_students = len(sheet_data)
    
    # Here's the plan to verify table pagination functionality:
    #
    # 1. We capture whatever students currently appear on the page
    # 2. We verify that the information matches what we extracted earlier
    # 3. If Next is not disabled, we click it
    # 4. Repeat steps 1 - 3 until Next is disabled
    # 5. Do the same for each additional option from the dropdown (5, 10, All)

    for dropdown_option in option_list:
        total_table_rows = 0
        all_rows = []
        # First, set the value in the dropdown box.
        paginated_table_page.page_size_dropdown.click()
        paginated_table_page.page_size_dropdown.select_option(label=dropdown_option)
        # Let's go through the table, clicking the Next button as needed, until we have a list containing all the rows.
        while total_table_rows < 10:
            rows = page.locator("#example tbody tr").all_inner_texts()
            all_rows += rows
            total_table_rows += len(rows)
            # The Next link is hilariously flaky. I have to check to see if it has gained the aria-disabled attribute and only click the
            # button if the attribute isn't there, or else a lot of things go sideways.
            aria_is_disabled = paginated_table_page.next_button.get_attribute("aria-disabled") == "true"
            if aria_is_disabled:
               pass
            else:
                paginated_table_page.next_button.click()
        # Let's make sure the number of rows equal the previously established number of students.
        assert total_table_rows == num_students
        # We'll capture the student name to use as a comparison against the "master list."
        for student_row in all_rows:
            student_row_data = student_row.split('\t')
            # Assigning the student name to a new variable for readability
            student_row_name = student_row_data[0]
            # Go through the "master list" until we find a match with our captured name. We assume unique names here.
            for student in sheet_data:
                if student["student_Name"] == student_row_name:
                    # Having found a match, we verify that the contents of each additional cell match.
                    assert student["gender"] == student_row_data[1]
                    assert student["class_Level"] == student_row_data[2]
                    assert student["home_State"] == student_row_data[3]
                    assert student["major"] == student_row_data[4]
                    assert student["extracurricular_Activity"] == student_row_data[5]

# Testing search capability. We'll give the search some sample data (including negatives) and make sure the criteria is found, or not found as appropriate.
# We'll represent the "correct" answers as a list of tuples.
search_test_cases = [
    ("Johnson", 1),
    ("Female", 5), # We'll have to click "Next" to ensure we have all the rows with this one.
    ("Skywalker", 0), # No one in the list is named Skywalker. Tragic!
    ("Freshman", 2),
    ("Ohio", 1),
]
@pytest.mark.parametrize("search_term, expected_count", search_test_cases)
def test_paginated_table_search(page: Page, search_term, expected_count):
    paginated_table_page = PaginatedTablePage(page)
        
    response = paginated_table_page.navigate()
    assert response.ok

    # Make sure the search field is visible.
    expect(paginated_table_page.search_input).to_be_visible()

    # Search using the function built on the POM page.
    search_results = paginated_table_page.execute_search(search_term)
    assert len(search_results) == expected_count

# Testing sorting capability. I'll make this a little easier on myself by displaying all table entries, eliminating the need to have to page through.
# Columns that are the "active" sorting column have the class "sorting_asc" or "sorting_desc" while non-sorting columns simply have the class "sorting".
def test_paginated_table_sort(page: Page):
    paginated_table_page = PaginatedTablePage(page)

    response = paginated_table_page.navigate()
    assert response.ok

    paginated_table_page.page_size_dropdown.select_option(label="All")
    rows = page.locator("#example tbody tr").all_inner_texts()
    assert len(rows) == 10

    # For each column in the title row, we'll make sure clicking it gives it the apporpriate class and then verify that the apropriate column is sorted properly.
    title_columns = paginated_table_page.student_title_row.locator("th").all()

    # The default table sort is by student name, ascending. We'll validate that first before moving through the other columns.
    column_cells = page.locator("table tbody tr td:nth-child(1)")
    column_values = [text.strip() for text in column_cells.all_inner_texts()]
    sorting = title_columns[0].get_attribute("aria-sort")
    assert sorting == "ascending"
    assert column_values == sorted(column_values, key=str.casefold)
    title_columns[0].click()
    column_values = [text.strip() for text in column_cells.all_inner_texts()]
    sorting = title_columns[0].get_attribute("aria-sort")
    assert sorting == "descending"
    assert column_values == sorted(column_values, key=str.casefold, reverse=True)
    column_index = 2
    for column in title_columns[1:]:
        column.click()
        column_cells = page.locator(f"table tbody tr td:nth-child({column_index})")
        column_values = [text.strip() for text in column_cells.all_inner_texts()]
        sorting = column.get_attribute("aria-sort")
        assert sorting == "ascending"
        assert column_values == sorted(column_values, key=str.casefold)
        column.click()
        column_cells = page.locator(f"table tbody tr td:nth-child({column_index})")
        column_values = [text.strip() for text in column_cells.all_inner_texts()]
        sorting = column.get_attribute("aria-sort")
        assert sorting == "descending"
        assert column_values == sorted(column_values, key=str.casefold, reverse=True)
        column_index = column_index + 1