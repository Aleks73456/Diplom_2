import requests
import allure
from helpers import BASE_URL
import helpers

class TestGetUserOrders:

    @allure.title('Проверка получения заказов пользователя с авторизацией')
    def test_get_auth_user_orders(self,regist):
        response = requests.get(f'{BASE_URL}/api/orders', headers = regist)
        assert response.status_code == 200
        assert 'orders' in response.json()

     
    @allure.title('Проверка получения заказов пользователя без авторизации')
    def test_get_user_orders_without_auth(self):
        response = requests.get(f'{BASE_URL}/api/orders')
        assert response.status_code == 401
        assert response.json()['message'] == "You should be authorised"
    