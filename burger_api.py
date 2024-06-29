import allure
import requests

import URLS


class BurgerApi:

    @allure.step('Создание юзера')
    def create_user(data):
        response = requests.post(URLS.CREATE_USER_URL, json=data)
        return response

    @allure.step('Логин юзера')
    def login_user(data):
        response = requests.post(URLS.LOGIN_USER_URL, json=data)
        return response

    @allure.step('Изменение данных юзера')
    def patch_user(data):
        response = requests.patch(URLS.USER_DATA_URL, json=data)
        return response

    @allure.step('Получение ингредиентов')
    def get_ingredients_list():
        response = requests.get(URLS.INGREDIENT_API)
        return response

    @allure.step('Создание заказа')
    def create_order(data):
        response = requests.post(URLS.ORDER_URL, json=data)
        return response

    @allure.step('Получение списка заказов')
    def get_order(self):
        response = requests.get(URLS.ORDER_URL)
        return response
