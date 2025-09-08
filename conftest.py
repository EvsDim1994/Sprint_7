import pytest

from src.helpers.reqistration_user import register_new_courier_and_return_login_password


@pytest.fixture(scope='function')
def сreate_courier():
    return register_new_courier_and_return_login_password()