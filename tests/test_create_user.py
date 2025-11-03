import requests
import allure
from helpers import BASE_URL
import helpers

class TestRegisterUser:

    @allure.title('Проверка регистрации пользователя')
    def test_register_user(self):
        payload = helpers.payload_for_regist()
        response = requests.post(f'{BASE_URL}/api/auth/register', json=payload)
        assert response.status_code == 200
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()
        helpers.delete_user(response.json()['accessToken'])

    @allure.title('Проверка повторной регистрации пользователя')
    def test_register_dublicate_user(self):
        payload = helpers.payload_for_regist()
        response= requests.post(f'{BASE_URL}/api/auth/register', json=payload)
        response_two = requests.post(f'{BASE_URL}/api/auth/register', json=payload)
        assert response_two.status_code == 403
        assert response_two.json()['message'] == 'User already exists'
        helpers.delete_user(response.json()['accessToken'])

    @allure.title('Проверка регистрации без указания email')
    def test_register_user_without_by_email(self):
        payload = helpers.payload_for_regist_invalid()
        response = requests.post(f'{BASE_URL}/api/auth/register', json=payload)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
