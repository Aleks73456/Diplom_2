import requests
import string
import random
import allure



BASE_URL = 'https://stellarburgers.education-services.ru'


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

@allure.step('Регистрируем пользователя, чтобы получить его accessToken')
def regist_user_for_get_access_token():
        email = f"{generate_random_string(10)}@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)
        payload = {"email": email , "password": password, "name": name}
        response =requests.post(f'{BASE_URL}/api/auth/register', json=payload)
        return response.json()['accessToken']

@allure.step('Регистрируем пользователя, чтобы получить его email и password для авторизации')
def regist_user_for_login():
        email = f"{generate_random_string(10)}@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)
        payload = {"email": email , "password": password, "name": name}
        requests.post(f'{BASE_URL}/api/auth/register', json=payload)
        return {
            "email": email,
            "password": password
        }

@allure.step('Генерируем тело для регистрации')
def payload_for_regist():
        email = f"{generate_random_string(10)}@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)
        payload = {"email": email , "password": password, "name": name}
        return payload

@allure.step('Генерируем тело для негативной проверки')
def payload_for_regist_invalid():
        password = generate_random_string(10)
        name = generate_random_string(10)
        payload = {"password": password, "name": name}
        return payload

@allure.step('Удаляем пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    response = requests.delete(f'{BASE_URL}/api/auth/user', headers=headers)
    return response


def payload_for_create_order():
    payload ={"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
    return payload

def invalid_payload_for_create_order():
       payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6f","61c0c5a71d1f820016f"]}
       return payload

def payload_for_change_user_data():
       payload = {"name": "dsfsf"}
       return payload

def invalid_payload_for_login_user():
       email ="dsfs@yandex.ru"
       password = "2dre"
       login_payload = {"email": email , "password": password}
       return login_payload