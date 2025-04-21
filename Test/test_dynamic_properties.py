
def test_visible_after_5_seconds(driver, dynamic_props_page):
    dynamic_props_page.go_to()
    assert dynamic_props_page.wait_for_visible_button()

def test_color_change(driver, dynamic_props_page):
    dynamic_props_page.go_to()
    assert dynamic_props_page.detect_color_change()
