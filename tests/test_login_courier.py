import allure
import requests
from src.helpers.reqistration_user import generate_random_string
from src.path import Path


class TestLoginCourier:
        
    def test_successfull_login_courier(self, сreate_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": сreate_courier[0],
                    "password": сreate_courier[1]
                }

            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 200
                assert response.json()["id"] > 0


    def test_unsuccessfull_login_courier_without_password_field(self, сreate_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": сreate_courier[0]
                }
            
            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 400
                assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


    def test_unsuccessfull_login_courier_without_login_field(self, сreate_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "password": сreate_courier[1]
                }
            
            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 400
                assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    
    def test_unsuccessfull_login_courier_with_incorrect_password(self, сreate_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": сreate_courier[0],
                    "password": "111"
                }

            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 404
                assert response.json()["message"] == "Учетная запись не найдена"


    def test_unsuccessfull_login_courier_with_incorrect_login(self, сreate_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": "111",
                    "password": сreate_courier[1]
                }

            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 404
                assert response.json()["message"] == "Учетная запись не найдена"
