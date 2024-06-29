import allure
import requests
import URLS
from helper import OrderGenerate


class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_by_auth_user(self, unique_user_for_changing):
        user, token = unique_user_for_changing
        data = OrderGenerate.generate_orger_list()
        order = requests.post(URLS.ORDER_URL, data=data, headers={'Authorization': token})
        requests.delete(URLS.USER_DATA_URL, headers={'Authorization': token})
        assert order.status_code == 200 and order.json()['success'] is True

    @allure.title('Создание заказа неавторизованным пользователем. Баг бэка: не возвращает ошибку')
    def test_create_order_by_not_auth_user(self):
        data = OrderGenerate.generate_orger_list()
        order = requests.post(URLS.ORDER_URL, data=data)
        assert order.status_code == 401 and order.json()['message'] == "You should be authorised"

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_no_ingredients(self, unique_user_for_changing):
        user, token = unique_user_for_changing
        data = {"ingredients": ''}
        order = requests.post(URLS.ORDER_URL, data=data, headers={'Authorization': token})
        requests.delete(URLS.USER_DATA_URL, headers={'Authorization': token})
        assert order.status_code == 400 and order.json()['message'] == "Ingredient ids must be provided"

    @allure.title('Создание заказа с невалидным хешем ингредиентов')
    def test_create_order_invalid_hash_ingredients(self, unique_user_for_changing):
        user, token = unique_user_for_changing
        data = {"ingredients": 123456}
        order = requests.post(URLS.ORDER_URL, data=data, headers={'Authorization': token})
        requests.delete(URLS.USER_DATA_URL, headers={'Authorization': token})
        assert order.status_code == 500
