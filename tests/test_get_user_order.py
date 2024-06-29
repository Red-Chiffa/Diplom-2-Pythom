import allure
import requests
import URLS


class TestGetUserOrder:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_auth_user_order_list(self, unique_user_for_changing):
        user, token = unique_user_for_changing
        order_list = requests.get(URLS.ORDER_URL, headers={'Authorization': token})
        assert order_list.status_code == 200 and order_list.json()['success'] is True

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_not_auth_user_order_list(self, unique_user_for_changing):
        order_list = requests.get(URLS.ORDER_URL)
        assert order_list.status_code == 401 and order_list.json()['message'] == "You should be authorised"
