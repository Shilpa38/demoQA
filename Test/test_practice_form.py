# tests/test_practice_form.py

def test_required_field_validation(driver, practice_form_page):
    practice_form_page.go_to()
    practice_form_page.submit_empty_form(driver)
    assert practice_form_page.is_validation_displayed("First Name")
