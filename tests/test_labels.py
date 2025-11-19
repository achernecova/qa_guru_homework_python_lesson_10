from allure_commons.types import Severity

import allure

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
