import allure
import pytest
import requests

from src.path import Path


class TestCreateOrder:
        
    @pytest.mark.parametrize('color', 
        [
            ["BLACK", "GREY"],  # список с двумя цветами
            [],                 # пустой список цветов
            ["BLACK"]           # список с одним цветом
        ])    
    def test_successfull_create_order(self, color):
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
                "color": color
            }
        with allure.step("отправляем запрос на создание заказа и сохраняем ответ в переменную response"): 
            response = requests.post(Path.ORDER, data=payload)
        with allure.step("проверка кода и тела ответа"): 
            assert response.status_code == 201
            assert response.json()["track"] > 0
            