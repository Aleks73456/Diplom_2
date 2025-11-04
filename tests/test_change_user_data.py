import requests
import allure
from helpers import BASE_URL
import helpers

class TestChangeUserData:

    
    
    @allure.title('Проверка изменения данных пользователя с авторизацией')
    def test_change_user_data(self,regist):
        payload = helpers.payload_for_change_user_data()
        response = requests.patch(f'{BASE_URL}/api/auth/user',json = payload, headers = regist)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "dsfsf"

        
    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_change_user_data_without_auth(self):
        payload = helpers.payload_for_change_user_data()
        response = requests.patch(f'{BASE_URL}/api/auth/user',json = payload)
        assert response.status_code == 401
        assert response.json()["message"] == helpers.ERROR_USER_MUST_BE_AUTH
