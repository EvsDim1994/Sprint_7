import pytest

from src.helpers.delete_user import delete_registrationed_user
from src.helpers.reqistration_user import register_new_courier_and_return_login_password
from src.models.users import Courier


@pytest.fixture(scope='class')
def create_courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    courier = Courier(login, password)
    yield courier
    if courier.user_id > 0:
        delete_registrationed_user(courier.user_id)