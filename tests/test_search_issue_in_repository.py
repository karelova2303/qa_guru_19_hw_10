import allure
from allure_commons.types import Severity
from selene import browser, by, have, be
from selene.support.shared.jquery_style import s

from pages.search_issue import Issue

repository = 'eroshenkoam/allure-playwright-example'
actual_text = 'Не работает переход по табу Issues'


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'karelova2303')
@allure.feature('Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
# Тест №1. Чистый Selene (без шагов)
def test_search_issue_simple(setup_browser):
    browser.open('/')

    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repository).press_enter()

    s(by.link_text(repository)).click()

    s('#issues-tab').click()

    s(by.text(actual_text)).should(be.visible)


# Тест №2. Лямбда шаги через with allure.step
@allure.tag('Web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'karelova2303')
@allure.feature(f'Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_search_issue_with_steps(setup_browser):
    with allure.step('Открываем главную страницу GitHub'):
        browser.open('/')

    with allure.step(f'Ищем репозиторий {repository}'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys(repository).press_enter()

    with allure.step(f'Переходим по ссылке репозитория {repository}'):
        s(by.link_text(repository)).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step(f'Проверяем отображение задачи с текстом "{actual_text}"'):
        s(by.text(actual_text)).should(be.visible)


# Тест №3. Шаги с декоратором @allure
@allure.tag('Web', 'Dev')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'karelova2303')
@allure.feature(f'Задачи в репозитории')
@allure.story(f'Неавторизованный пользователь проверяет наличие задачи в репозитории')
@allure.link('https://github.com')
def test_search_issue_with_steps_decorator(setup_browser):
    issue = Issue()

    issue.open_main_page()
    issue.search_for_repository(repository)
    issue.go_to_repository(repository)
    issue.open_issue_tab()
    issue.should_see_issue_with_text(actual_text)
