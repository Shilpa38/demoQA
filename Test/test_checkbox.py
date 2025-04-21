def test_checkbox_tree(driver, checkbox_page):
    checkbox_page.go_to()
    checkbox_page.expand_all(driver)
    checkbox_page.select_parent("Documents")
    assert checkbox_page.are_nested_checkboxes_selected("Documents")
