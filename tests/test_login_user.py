import requests
import allure
from helpers import BASE_URL
import helpers


class TestLoginUser:
      
    @allure.title('Проверка авторизации пользователя')
    def test_login_user(self):
        login_payload = helpers.regist_user_for_login()
        response = requests.post(f'{BASE_URL}/api/auth/login',json = login_payload)
        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        helpers.delete_user(response.json()['accessToken'])
    
    @allure.title('Проверка авторизации пользователя с некорректными данными')
    def test_login_invalid_password_and_email_user(self):
        login_payload = helpers.invalid_payload_for_login_user()
        response = requests.post(f'{BASE_URL}/api/auth/login',json = login_payload)
        assert response.status_code == 401
        assert response.json()['message'] == helpers.ERROR_EMAIL_OR_PASSWORD_INCORRECT
        