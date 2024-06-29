import allure
import pytest
import requests

import URLS
from burger_api import BurgerApi
from helper import UserGenerate


@pytest.fixture
@allure.step('Создание уникального пользователя и его регистрация с последующим удалением')
def unique_user():
    generated_user = UserGenerate.generate_body_fake_user()
    response = BurgerApi.create_user(generated_user)
    token = response.json()['accessToken']
    requests.delete(URLS.USER_DATA_URL, headers={'Authorization': token})
    return response


@pytest.fixture
@allure.step('Создание уникального пользователя и его регистрация')
def unique_user_for_changing():
    generated_user = UserGenerate.generate_body_fake_user()
    response = BurgerApi.create_user(generated_user)
    token = response.json()['accessToken']
    return response, token
