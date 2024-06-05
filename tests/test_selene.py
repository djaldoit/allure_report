from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("/")

    s(".search-input").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("Issue for HW qa.guru")).should(be.visible)
