import allure
import pytest
import random
import requests
import URLS
from data import UserData


class TestChangeUserData:
    change_data = [['email', f"sasha{random.randint(0, 100000)}@ya.ru"],
                   ['password', random.randint(100000, 999999)],
                   ['name', 'qwerty']]

    @allure.title('Изменение данных авторизованного пользователя')
    @pytest.mark.parametrize('key, value', change_data)
    def test_change_auth_user_data(self, unique_user_for_changing, key, value):
        user, token = unique_user_for_changing
        body = requests.get(URLS.USER_DATA_URL, headers={'Authorization': token})
        change_body = body.json().copy()
        change_body[key] = value
        changed_data = requests.patch(URLS.USER_DATA_URL,
                                      data=change_body,
                                      headers={'Authorization': token})
        requests.delete(URLS.USER_DATA_URL, headers={'Authorization': token})
        assert changed_data.status_code == 200 and changed_data.json()['success'] is True

    @allure.title('Изменение данных неавторизованного пользователя')
    def test_change_auth_not_user_data(self):
        changed_data = requests.patch(URLS.USER_DATA_URL,
                                      data=UserData.LOGIN_BODY)
        assert changed_data.status_code == 401 and changed_data.json()['message'] == "You should be authorised"
