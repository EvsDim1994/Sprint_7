# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
import allure
import requests

from src.path import Path


def delete_registrationed_user(user_id):

    with allure.step("отправляем запрос на удаление курьера и сохраняем ответ в переменную response"): 
        response = requests.delete(Path.CREATE_COURIER + f"/{user_id}")
    with allure.step("проверка кода ответа"):
        assert response.status_code == 200
        