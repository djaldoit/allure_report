import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозитория"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с названием 'Another tests issue'"):
        s(by.partial_text("Issue for HW qa.guru")).should(be.visible)
