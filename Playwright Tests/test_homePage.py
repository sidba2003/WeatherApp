from playwright.sync_api import expect
from playwright.sync_api import Page


def test_has_expected_title_and_headers(page: Page):
    page.goto("http://localhost:5000/")

    expect(page).to_have_title("Weather App")

    heaadLocator = page.locator("h1")
    expect(heaadLocator).to_have_text("London")


def test_has_table_and_correct_table_rows(page: Page):
    page.goto("http://localhost:5000/")

    locatorTable = page.locator(".stats")
    locatorTable.is_visible()

    locatorTable = page.locator(".stat")
    expect(locatorTable).to_have_count(7)


def test_has_correct_button_layout_and_values(page: Page):
    page.goto("http://localhost:5000/")

    layoutLocator = page.locator(".chooseparks")
    layoutLocator.is_visible()

    buttonLocator = layoutLocator.locator(".btn")
    expect(buttonLocator).to_have_count(3)

    expect(buttonLocator.nth(0)).to_have_text("Thorpe park")
    expect(buttonLocator.nth(1)).to_have_text("Alton Towers")
    expect(buttonLocator.nth(2)).to_have_text("Blackpool amusement park")
