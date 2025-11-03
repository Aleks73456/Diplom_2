import requests
import allure
from helpers import BASE_URL
import helpers

class TestChangeUserData:

    
    
    @allure.title('Проверка изменения данных пользователя с авторизацией')
    def test_change_user_data(self):
        access_token = helpers.regist_user_for_get_access_token()
        auth = {'Authorization': access_token}
        payload = helpers.payload_for_change_user_data()
        response = requests.patch(f'{BASE_URL}/api/auth/user',json = payload, headers = auth)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == "dsfsf"
        helpers.delete_user(access_token)
        
    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_change_user_data_without_auth(self):
        payload = helpers.payload_for_change_user_data()
        response = requests.patch(f'{BASE_URL}/api/auth/user',json = payload)
        assert response.status_code == 401
        assert response.json()["message"] == "You should be authorised"
