from pages.home_page import HomePage

def test_search_functionality(driver):
    driver.get("https://example.com")
    home = HomePage(driver)
    home.search("pytest selenium")
    assert "Search Results" in driver.title
