from time import sleep

from selene import be, browser, by
from selene.support.shared.jquery_style import s

import allure

# Пишем тест на гитхаб - eroshenkoam/allure-example - проваливаемся в первую репу.
# Ищем issues - и его там нет. Что делать?... Возьмем id = pull-requests-tab


def test_dynamic_github():

    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        # sleep(60)
        s(".FormControl-input").send_keys("eroshenkoam/allure-example")
        sleep(5)
        s(".FormControl-input").submit()

    sleep(5)
    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()
    sleep(5)
    with allure.step("Кликаем по табу requests"):
        s("#pull-requests-tab").click()
    sleep(5)
    with allure.step("Проверяем, что есть Pull request с номером #91"):
        s(by.partial_text("#90")).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repositiry("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_tab()
    should_see_requests_with_number("91")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repositiry(repo):
    s(".header-search-button").click()
    # sleep(60)
    s(".FormControl-input").send_keys(repo)
    sleep(5)
    s(".FormControl-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Кликаем по табу requests")
def open_tab():
    s("#pull-requests-tab").click()


@allure.step("Проверяем, что есть Pull request с номером {number}")
def should_see_requests_with_number(number):
    s(by.partial_text("#" + number)).should(be.visible)
