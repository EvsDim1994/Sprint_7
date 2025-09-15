from src.config import Config


class Path:
    CREATE_COURIER = Config.URL + "api/v1/courier"
    LOGIN = Config.URL + "api/v1/courier/login"
    ORDER = Config.URL + "api/v1/orders"
    ORDER_ACCEPT = Config.URL + "api/v1/orders/accept"
    TRACK = Config.URL + "api/v1/orders/track"
    