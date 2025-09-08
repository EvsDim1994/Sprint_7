from asyncio.windows_events import NULL
import requests
from src.api.helpers.reqistration_user import generate_random_string


class TestCreateCoirier:
        
    def test_successfull_create_courier(self):
            # генерируем логин, пароль и имя курьера
            login = generate_random_string(10)
            password = generate_random_string(10)
            first_name = generate_random_string(10)
            
            # собираем тело запроса
            payload = {
                "login": login,
                "password": password,
                "firstName": first_name
            }

            # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
            response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
            # проверка кода и тела ответа
            assert response.status_code == 201
            assert response.json()["ok"] == True


    def test_unsuccessfull_create_courier_with_the_same_data(self):
            # генерируем логин, пароль и имя курьера
            login = generate_random_string(10)
            password = generate_random_string(10)
            first_name = generate_random_string(10)

            # собираем тело запроса
            payload = {
                "login": login,
                "password": password,
                "firstName": first_name
            }

            # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
            response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
            # проверка кода ответа
            assert response.status_code == 201
            # отправляем повторный запрос на регистрацию курьера и сохраняем ответ в переменную response_with_the_same_data
            response_with_the_same_data = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
            # проверка кода и тела ответа
            assert response_with_the_same_data.status_code == 409
            assert response_with_the_same_data.json()["message"] == "Этот логин уже используется"


    def test_create_courier_without_login(self):
            # генерируем пароль и имя курьера
            password = generate_random_string(10)
            first_name = generate_random_string(10)
            
            # собираем тело запроса
            payload = {
                "password": password,
                "firstName": first_name
            }

            # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
            response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
            # проверка кода и тела ответа
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


    def test_create_courier_without_password(self):
            # генерируем логин и имя курьера
            login = generate_random_string(10)
            first_name = generate_random_string(10)
            
            # собираем тело запроса
            payload = {
                "login": login,
                "firstName": first_name
            }

            # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
            response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
            # проверка кода и тела ответа
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
  

