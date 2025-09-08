from asyncio.windows_events import NULL
import allure
import requests
from src.helpers.reqistration_user import generate_random_string
from src.path import Path


class TestCreateCoirier:
        
    def test_successfull_create_courier(self):
            with allure.step("генерируем логин, пароль и имя курьера"): 
                login = generate_random_string(10)
                password = generate_random_string(10)
                first_name = generate_random_string(10)
            
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": login,
                    "password": password,
                    "firstName": first_name
                }

            with allure.step("отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response"): 
                response = requests.post(Path.CREATE_COURIER, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 201
                assert response.json()["ok"] == True


    def test_unsuccessfull_create_courier_with_the_same_data(self):
            with allure.step("генерируем логин, пароль и имя курьера"): 
                login = generate_random_string(10)
                password = generate_random_string(10)
                first_name = generate_random_string(10)

            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": login,
                    "password": password,
                    "firstName": first_name
                }

            with allure.step("отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response"): 
                response = requests.post(Path.CREATE_COURIER, data=payload)
            with allure.step("проверка кода ответа"):
                assert response.status_code == 201
            with allure.step("отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response_with_the_same_data"): 
                response_with_the_same_data = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response_with_the_same_data.status_code == 409
                assert response_with_the_same_data.json()["message"] == "Этот логин уже используется"


    def test_create_courier_without_login(self):
            with allure.step("генерируем пароль и имя курьера"): 
                password = generate_random_string(10)
                first_name = generate_random_string(10)
            
            with allure.step("формирование тела запроса"): 
                payload = {
                    "password": password,
                    "firstName": first_name
                }

            with allure.step("отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response"): 
                response = requests.post(Path.CREATE_COURIER, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 400
                assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


    def test_create_courier_without_password(self):
            with allure.step("генерируем логин и имя курьера"): 
                login = generate_random_string(10)
                first_name = generate_random_string(10)
            
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": login,
                    "firstName": first_name
                }

            with allure.step("отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response"): 
                response = requests.post(Path.CREATE_COURIER, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 400
                assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
