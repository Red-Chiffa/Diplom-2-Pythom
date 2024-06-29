import allure
from faker import Faker
from burger_api import BurgerApi
import random


class UserGenerate:
    @staticmethod
    @allure.step('Геренация пользователя')
    def generate_body_fake_user():
        fake = Faker()

        return {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }

    @staticmethod
    @allure.step('Геренация пользователя для провверки авторизации с неверной парой логин-пароль')
    def generate_body_fake_user_for_login():
        fake = Faker()

        return {
            "email": fake.email(),
            "password": fake.password(),
        }


class OrderGenerate:
    pass

    @staticmethod
    @allure.step('Геренация списка ингредиентов для заказа')
    def generate_orger_list():
        base = BurgerApi.get_ingredients_list()
        quantity_ingredients = len(base.json()['data'])
        order_ingredients = []
        order_ingredients.append(base.json()['data'][random.randint(1, quantity_ingredients)]['_id'])
        order_ingredients.append(base.json()['data'][random.randint(1, quantity_ingredients)]['_id'])
        order_ingredients.append(base.json()['data'][random.randint(1, quantity_ingredients)]['_id'])
        order_ingredients.append(base.json()['data'][random.randint(1, quantity_ingredients)]['_id'])
        return {"ingredients": order_ingredients}
