import requests
import allure
from helpers import BASE_URL
import helpers

class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_auth(self):
        access_token = helpers.regist_user_for_get_access_token()
        auth = {'Authorization': access_token}
        payload = helpers.payload_for_create_order()
        response = requests.post(f'{BASE_URL}/api/orders',json = payload, headers = auth)
        assert response.status_code == 200
        assert 'order' in response.json()
        helpers.delete_user(access_token)

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_auth(self):
        payload = helpers.payload_for_create_order()
        response = requests.post(f'{BASE_URL}/api/orders',json = payload)
        assert response.status_code == 200
        assert 'order' in response.json()
    
    @allure.title('Проверка создания заказа без указания ингредиентов')
    def test_create_order_without_ingredients(self):
        access_token = helpers.regist_user_for_get_access_token()
        auth = {'Authorization': access_token}
        response = requests.post(f'{BASE_URL}/api/orders', headers = auth)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"
        helpers.delete_user(access_token)
    
    @allure.title('Проверка создания заказа с указанием несущестсвующих ингредиентов')
    def test_create_order_invalid_ingredients(self):
        access_token = helpers.regist_user_for_get_access_token()
        auth = {'Authorization': access_token}
        payload = helpers.invalid_payload_for_create_order()
        response = requests.post(f'{BASE_URL}/api/orders',json = payload, headers = auth)
        assert response.status_code == 500
        helpers.delete_user(access_token)
      
