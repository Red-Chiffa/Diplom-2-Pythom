import random

import allure
import pytest
from burger_api import BurgerApi
from data import UserData


class TestCreateUser:
    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, unique_user):
        created_user = unique_user
        assert created_user.status_code == 200 and created_user.json()['success'] is True

    @allure.title('Создание неуникального пользователя')
    def test_create_non_unique_user(self):
        created_user = BurgerApi.create_user(UserData.LOGIN_BODY)
        assert created_user.status_code == 403 and created_user.json()['message'] == "User already exists"

    incomplete_data = [[f"sasha{random.randint(0, 100000)}@ya.ru", random.randint(100000, 999999), ''],
                       [f"sasha{random.randint(0, 100000)}@ya.ru", '', 'Саша'],
                       ['', random.randint(100000, 999999), 'Саша']]

    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize('email, password, name', incomplete_data)
    def test_create_incomplete_data_user(self, email, password, name):
        body = {"email": email, "password": password, "name": name}
        created_user = BurgerApi.create_user(body)
        assert created_user.status_code == 403 and created_user.json()['message'] == ("Email, password and name are "
                                                                                      "required fields")
