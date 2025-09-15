import allure
import requests
import logging

from src.helpers.validatate_json import assertion_validate_structure
from src.models.orders import ApiResponse
from src.path import Path


class TestGetOrderByNumbers:
        
    def test_successfull_get_orders_by_numbers(self):
        with allure.step("формирование тела запроса"): 
            payload = {
                "firstName": "Naruto",
                "lastName": "Uchiha",
                "address": "Konoha, 142 apt.",
                "metroStation": 4,
                "phone": "+7 800 355 35 35",
                "rentTime": 5,
                "deliveryDate": "2020-06-06",
                "comment": "Saske, come back to Konoha",
                "color": ["BLACK", "GREY"] 
            }
        with allure.step("отправляем запрос на создание заказа и сохраняем ответ в переменную response"): 
            response = requests.post(Path.ORDER, data=payload)
        with allure.step("проверка кода и тела ответа"): 
            assert response.status_code == 201
            assert response.json()["track"] > 0
            order_id = response.json()["track"]
        with allure.step("проверка кода и тела ответа"):
            params = {"t": order_id}
            response_order_by_number = requests.get(Path.TRACK, params=params)
            print(f"Request URL: {Path.TRACK}, params: {params}")
            print(f"Response status: {response_order_by_number.status_code}")
            print(f"Response body: {response_order_by_number.json()}")
            assert response_order_by_number.status_code == 200
            assertion_validate_structure(response_order_by_number.json(), ApiResponse)
            