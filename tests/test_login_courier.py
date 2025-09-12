import allure
import requests
from src.errors import Errors
from src.helpers.reqistration_user import generate_random_string
from src.path import Path


class TestLoginCourier:
        
    def test_successfull_login_courier(self, create_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": create_courier.login,
                    "password": create_courier.password
                }

            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                create_courier.user_id = response.json()["id"]
                assert response.status_code == 200
                assert response.json()["id"] > 0


    def test_unsuccessfull_login_courier_without_password_field(self, create_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": create_courier.login
                }
            
            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 400
                assert response.json()["message"] == Errors.LOGIN_ERROR_WITHOUT_FILEDS


    def test_unsuccessfull_login_courier_without_login_field(self, create_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "password": create_courier.password
                }
            
            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"):
                assert response.status_code == 400
                assert response.json()["message"] == Errors.LOGIN_ERROR_WITHOUT_FILEDS

    
    def test_unsuccessfull_login_courier_with_incorrect_password(self, create_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": create_courier.login,
                    "password": "111"
                }

            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 404
                assert response.json()["message"] == Errors.LOGIN_ERROR


    def test_unsuccessfull_login_courier_with_incorrect_login(self, create_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": "111",
                    "password": create_courier.password
                }

            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 404
                assert response.json()["message"] == Errors.LOGIN_ERROR
