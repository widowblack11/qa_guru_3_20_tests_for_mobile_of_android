import allure
from allure import step as title
from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure import step


@allure.title("Wikipedia search BrowserStack")
def test_search():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'BrowserStack'
        )

    with step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))


@allure.title("Wikipedia search selene and go to page")
def test_search_selene():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("python")
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()
    browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('An error occurred'))
