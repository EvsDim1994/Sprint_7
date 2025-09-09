import allure
import requests

from src.errors import Errors
from src.path import Path


class TestAcceptOrder:
           
    def test_successfull_accept_order(self, create_courier):
        with allure.step("отправляем запрос на получение списка заказов и сохраняем ответ в переменную response_order"): 
            response_order = requests.get(Path.ORDER)
        with allure.step("проверка кода и тела ответа"): 
            assert response_order.status_code == 200
        with allure.step("сохранение id заказ в переменную id_order"): 
            id_order = response_order.json()["orders"][0]["id"]
        with allure.step("формирование тела запроса"): 
                payload_courier = {
                    "login": create_courier.login,
                    "password": create_courier.password
                }

        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_login"): 
            response_login = requests.post(Path.LOGIN, data=payload_courier)
        with allure.step("проверка кода и тела ответа"): 
            create_courier.user_id = response_login.json()["id"]
            assert response_login.status_code == 200
        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_accept_order"): 
            params = {"courierId": create_courier.user_id}
            response_accept_order = requests.put(Path.ORDER_ACCEPT + f"/{id_order}", params=params)
        with allure.step("проверка кода и тела ответа"): 
            assert response_accept_order.status_code == 200
            assert response_accept_order.json()["ok"] == True


    def test_unsuccessfull_accept_order_without_id_courier(self):
        with allure.step("отправляем запрос на получение списка заказов и сохраняем ответ в переменную response_order"): 
            response_order = requests.get(Path.ORDER)
        with allure.step("проверка кода и тела ответа"): 
            assert response_order.status_code == 200
        with allure.step("сохранение id заказ в переменную id_order"): 
            id_order = response_order.json()["orders"][0]["id"]
        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_accept_order"): 
            params = {"courierId": ""}
            response_accept_order = requests.put(Path.ORDER_ACCEPT + f"/{id_order}", params=params)
        with allure.step("проверка кода и тела ответа"): 
            assert response_accept_order.status_code == 400
            assert response_accept_order.json()["message"] == Errors.ACCEPT_ORDER_WITHOUT_IDS

        
    def test_unsuccessfull_accept_order_without_id_order(self, create_courier):
        with allure.step("формирование тела запроса"): 
                payload_courier = {
                    "login": create_courier.login,
                    "password": create_courier.password
                }

        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_login"): 
            response_login = requests.post(Path.LOGIN, data=payload_courier)
        with allure.step("проверка кода и тела ответа"): 
            create_courier.user_id = response_login.json()["id"]
            assert response_login.status_code == 200
        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_accept_order"): 
            params = {"courierId": create_courier.user_id}
            response_accept_order = requests.put(Path.ORDER_ACCEPT, params=params)
        with allure.step("проверка кода и тела ответа"): 
            assert response_accept_order.status_code == 400
            assert response_accept_order.json()["message"] == Errors.ACCEPT_ORDER_WITHOUT_IDS


    def test_unsuccessfull_accept_order_with_inccorect_id_courier(self):
        with allure.step("отправляем запрос на получение списка заказов и сохраняем ответ в переменную response_order"): 
            response_order = requests.get(Path.ORDER)
        with allure.step("проверка кода и тела ответа"): 
            assert response_order.status_code == 200
        with allure.step("сохранение id заказ в переменную id_order"): 
            id_order = response_order.json()["orders"][0]["id"]
        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_accept_order"): 
            params = {"courierId": "111"}
            response_accept_order = requests.put(Path.ORDER_ACCEPT + f"/{id_order}", params=params)
        with allure.step("проверка кода и тела ответа"): 
            assert response_accept_order.status_code == 404
            assert response_accept_order.json()["message"] == Errors.ACCEPT_ORDER_WITH_INCORRECT_ID_COURIER

        
    def test_unsuccessfull_accept_order_with_inccorect_id_order(self, create_courier):
        with allure.step("формирование тела запроса"): 
                payload_courier = {
                    "login": create_courier.login,
                    "password": create_courier.password
                }

        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_login"): 
            response_login = requests.post(Path.LOGIN, data=payload_courier)
        with allure.step("проверка кода и тела ответа"): 
            create_courier.user_id = response_login.json()["id"]
            assert response_login.status_code == 200
        with allure.step("отправляем запрос на логин и сохраняем ответ в переменную response_accept_order"): 
            params = {"courierId": create_courier.user_id}
            response_accept_order = requests.put(Path.ORDER_ACCEPT + "/111", params=params)
        with allure.step("проверка кода и тела ответа"): 
            assert response_accept_order.status_code == 404
            assert response_accept_order.json()["message"] == Errors.ACCEPT_ORDER_WITH_INCORRECT_ID_ORDER