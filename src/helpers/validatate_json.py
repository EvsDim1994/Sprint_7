from pydantic import BaseModel, ValidationError
from typing import Dict, Any, Type

def assertion_validate_structure(data: Dict[str, Any], dataclass_type: Type[BaseModel]) -> None:
    """
    Проверяет структуру словаря с данными с использованием указанной Pydantic-модели.
    Выбрасывает AssertionError, если данные не соответствуют модели.

    Args:
        data: Словарь с данными для валидации.
        dataclass_type: Класс Pydantic-модели для валидации (наследник BaseModel).

    Raises:
        AssertionError: Если данные не соответствуют модели.
        TypeError: Если dataclass_type не является Pydantic-моделью или data не словарь.
    """
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    if not issubclass(dataclass_type, BaseModel):
        raise TypeError("dataclass_type must be a Pydantic BaseModel subclass")

    try:
        # Пытаемся валидировать данные
        dataclass_type.model_validate(data)
    except ValidationError as e:
        # Преобразуем ошибку валидации в AssertionError с подробным сообщением
        raise AssertionError(f"Data structure validation failed: {e}") from e
    