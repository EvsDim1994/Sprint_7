from src.config import Config


class Path:
    CREATE_COURIER = Config.URL + "api/v1/courier"
    LOGIN = Config.URL + "api/v1/courier/login"
    MAKE_ORDER = Config.URL + "api/v1/orders"