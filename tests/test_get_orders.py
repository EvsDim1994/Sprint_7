import allure
import requests
from src.path import Path


class TestGetOrders:
        
    def test_successfull_get_orders(self):
            with allure.step("отправляем запрос на получение списка заказов и сохраняем ответ в переменную response"): 
                response = requests.get(Path.ORDER)
            with allure.step("проверка кода и тела ответа"): 
                assert response.status_code == 200
                assert len(response.json()["orders"]) > 0
                