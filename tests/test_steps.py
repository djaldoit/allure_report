import allure
from selene import browser, by
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_name("Issue for HW qa.guru")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("/")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с названием 'Another tests issue'")
def should_see_issue_with_name(name):
    s(by.partial_text(name)).click()