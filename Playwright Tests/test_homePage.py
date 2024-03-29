import re

from playwright.sync_api import expect
from playwright.sync_api import Page


def test_has_expected_title(page: Page):
    page.goto("https://localhost:5000")

    expect(page).to_have_title(re.compile("Weather App"))

def test_has_expected_heading(page: Page):
    page.goto("https://localhost:5000")

    expect(page).to_have_text("Weather App")
