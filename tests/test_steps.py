from time import sleep

import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s


# Пишем тест на гитхаб - eroshenkoam/allure-example - проваливаемся в первую репу.
# Ищем issues - и его там нет. Что делать?... Возьмем id = pull-requests-tab

# Взяла другую репу, где есть issues
def test_dynamic_github():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s(".FormControl-input").send_keys("eroshenkoam/allure-playwright-example")
        s(".FormControl-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-playwright-example")).click()

    with allure.step("Кликаем по табу Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем, что есть Issues с названием  Не работает переход по табу Issues"):
        s("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(
            have.exact_text("Не работает переход по табу Issues"))


# Issue скрыто для данного проекта
def test_decorator_steps():
    open_main_page()
    search_for_repositiry("eroshenkoam/allure-playwright-example")
    go_to_repository("eroshenkoam/allure-playwright-example")
    open_tab()
    should_see_requests_with_text("Не работает переход по табу Issues")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repositiry(repo):
    s(".header-search-button").click()
    s(".FormControl-input").send_keys(repo)
    s(".FormControl-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Кликаем по табу requests")
def open_tab():
    s("#issues-tab").click()


@allure.step("Проверяем, что есть Pull request с текстом {text}")
def should_see_requests_with_text(text):
    s("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(have.exact_text(f'{text}'
        ))
