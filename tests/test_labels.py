from allure_commons.types import Severity

import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s


# Пишем тест на гитхаб - eroshenkoam/allure-example - проваливаемся в первую репу.
# Ищем issues - и его там нет. Что делать?... Возьмем id = pull-requests-tab


def test_no_labels():
    pass


def test_dynamic_labels_github():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story(
        "Неавторизованный пользователь не может создать задачу в репозитории"
    )
    allure.dynamic.link("https://github.com", name="Testing")


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass



@allure.tag("normal")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "chernetsova")
@allure.feature("Проверка репозитория")
@allure.story("В репозитории есть вкладка Issues с записью")
@allure.link("https://github.com", name="Testing")
# Взяла другую репу, где есть issues
def test_label_issues_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s(".FormControl-input").send_keys("eroshenkoam/allure-playwright-example")
    s(".FormControl-input").submit()

    s(by.link_text("eroshenkoam/allure-playwright-example")).click()
    s("#issues-tab").click()

    s("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(
        have.exact_text("Не работает переход по табу Issues"))
