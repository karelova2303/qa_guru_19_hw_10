import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s

# Класс для теста №3
class Issue:

    @allure.step('Открываем главную страницу GitHub')
    def open_main_page(self):
        browser.open('https://github.com')

    @allure.step(f'Ищем репозиторий')
    def search_for_repository(self, repository):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys(repository).press_enter()

    @allure.step(f'Переходим по ссылке репозитория')
    def go_to_repository(self, repository):
        s(by.link_text(repository)).click()

    @allure.step('Открываем таб Issues')
    def open_issue_tab(self):
        s('#issues-tab').click()

    @allure.step(f'Проверяем отображение задачи с текстом')
    def should_see_issue_with_text(self, actual_text):
        s(by.text(actual_text)).should(be.visible)
