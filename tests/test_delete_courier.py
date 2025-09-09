import allure
import requests

from src.errors import Errors
from src.path import Path


class TestDeleteCourier:
        
    def test_successfull_delete_courier(self, create_courier):
            with allure.step("формирование тела запроса"): 
                payload = {
                    "login": create_courier.login,
                    "password": create_courier.password
                }

            with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response"): 
                response = requests.post(Path.LOGIN, data=payload)
            with allure.step("отправляем запрос на удаление курьера и сохраняем ответ в переменную response_delete"):
                user_id = response.json()["id"]
                response_delete = requests.delete(Path.CREATE_COURIER + f"/{user_id}")
            with allure.step("проверка кода и тела ответа"): 
                assert response_delete.status_code == 200
                assert response_delete.json()["ok"] == True


    def test_unsuccessfull_delete_courier_without_id(self):
            with allure.step("отправляем запрос на удаление курьера и сохраняем ответ в переменную response"):
                response = requests.delete(Path.CREATE_COURIER + f"/")
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 400
                assert response.json()["message"] == Errors.DELETE_ERROR


    def test_unsuccessfull_delete_courier_with_incorrect_id(self):
            with allure.step("отправляем запрос на удаление курьера и сохраняем ответ в переменную response"):
                response = requests.delete(Path.CREATE_COURIER + f"/111")
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 404 
                assert response.json()["message"] == Errors.DELETE_ERROR_WITH_INCORRECT_ID

