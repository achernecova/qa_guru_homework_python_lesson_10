from selene import be, browser, by, have
from selene.support.shared.jquery_style import s

# Пишем тест на гитхаб - eroshenkoam/allure-example - проваливаемся в первую репу.
# Ищем issues - и его там нет. Что делать?... Возьмем id = pull-requests-tab


def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s(".FormControl-input").send_keys("eroshenkoam/allure-playwright-example")
    s(".FormControl-input").submit()
    s(by.link_text("eroshenkoam/allure-playwright-example")).click()
    s("#issues-tab").click()
    s("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(have.exact_text("Не работает переход по табу Issues"))

