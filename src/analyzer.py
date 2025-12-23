import json
import time
from typing import Optional, Dict, Any

def mock_http_request(
    endpoint: str,
    method: str = "GET",
    data: Optional[Dict] = None
) -> Dict[str, Any]:
    """
    Заглушка для HTTP-запроса к API.
    Возвращает фиктивные данные для тестирования.
    """
    time.sleep(0.1)
    
    # Фиктивные ответы для разных эндпоинтов
    mock_responses = {
        "/users": {
            "status": 200,
            "data": [
                {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
                {"id": 2, "name": "Петр Петров", "email": "petr@example.com"}
            ]
        },
        "/products": {
            "status": 200,
            "data": [
                {"id": 101, "name": "Ноутбук", "price": 50000},
                {"id": 102, "name": "Телефон", "price": 25000}
            ]
        }
    }
    
    # Возвращаем мок-данные или заглушку по умолчанию
    response = mock_responses.get(endpoint, {
        "status": 404,
        "data": None,
        "message": f"Эндпоинт {endpoint} не найден"
    })
    
    # Логируем "запрос"
    print(f"[MOCK] {method} {endpoint}")
    if data:
        print(f"[MOCK] Данные: {data}")
    
    return response

if __name__ == "__main__":
    # Тестируем заглушку
    users_response = mock_http_request("/users", "GET")
    print(f"Ответ API пользователей: {json.dumps(users_response, indent=2, ensure_ascii=False)}")
    
    products_response = mock_http_request("/products", "GET")
    print(f"\nОтвет API продуктов: {json.dumps(products_response, indent=2, ensure_ascii=False)}")
