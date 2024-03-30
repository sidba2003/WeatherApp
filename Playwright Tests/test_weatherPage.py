from playwright.sync_api import Page, expect


def homePageClickHelper(page: Page, buttonIndex: int):
    page.goto("http://localhost:5000/")

    button = page.locator(".btn")
    expect(button).to_have_count(3)

    button.nth(buttonIndex).click()

def test_thorpeParkButton(page: Page):
    homePageClickHelper(page, 0)
    expect(page).to_have_title("Weather App")

    header = page.locator("h1")
    expect(header).to_have_text("Weather in Thorpe Park")

    statsTable = page.locator(".stats")
    expect(statsTable).to_be_visible()

    stat = page.locator(".stat")
    expect(stat).to_have_count(7)

    activityTable = page.locator(".activities")
    expect(activityTable).to_be_visible()

    activity = page.locator(".activity")
    expect(activity).to_have_count(6)

    activityVideo = activityTable.locator("a")

    for activityNumber in range(activityVideo.count()):
        website = activityVideo.nth(activityNumber).get_attribute("href")[:24]
        assert website == "https://www.youtube.com/"

