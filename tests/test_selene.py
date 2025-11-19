from selene import be, browser, by
from selene.support.shared.jquery_style import s

# Пишем тест на гитхаб - eroshenkoam/allure-example - проваливаемся в первую репу.
# Ищем issues - и его там нет. Что делать?... Возьмем id = pull-requests-tab


def test_github():
    browser.open("https://github.com")

    s(".header-search-button").click()
    # sleep(60)
    s(".FormControl-input").send_keys("eroshenkoam/allure-example")
    # sleep(5)
    s(".FormControl-input").submit()

    # sleep(5)
    s(by.link_text("eroshenkoam/allure-example")).click()
    # sleep(5)
    s("#pull-requests-tab").click()
    # sleep(5)
    s(by.partial_text("#90")).should(be.visible)
