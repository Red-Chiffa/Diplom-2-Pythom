from burger_api import BurgerApi
from data import UserData
from helper import UserGenerate


class TestLoginUser:
    def test_login_user(self):
        response = BurgerApi.login_user(UserData.LOGIN_BODY)
        assert response.status_code == 200 and response.json()['success'] is True

    def test_wrong_login_password_login_user(self):
        body = UserGenerate.generate_body_fake_user_for_login()
        response = BurgerApi.login_user(body)
        assert response.status_code == 401 and response.json()['message'] == "email or password are incorrect"
