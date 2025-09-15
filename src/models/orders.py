from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

# Модель для order
class Order(BaseModel):
    id: int 
    firstName: str
    lastName: str
    address: str
    metroStation: str
    phone: str
    rentTime: int
    deliveryDate: datetime  # ISO формат даты
    track: int
    status: int
    color: List[str]  # список цветов
    comment: str
    cancelled: bool
    finished: bool
    inDelivery: bool
    courierFirstName: Optional[str] = None
    createdAt: datetime  # ISO формат даты
    updatedAt: datetime  # ISO формат даты

# Основная модель для всего ответа
class ApiResponse(BaseModel):
    order: Order
    