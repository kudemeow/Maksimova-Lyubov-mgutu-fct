from typing import List, Dict, Optional, Union
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    """Модель пользователя"""
    id: int
    name: str
    email: str
    created_at: datetime = datetime.now()

class MockDatabase:
    """
    Заглушка для базы данных.
    Хранит данные в памяти для тестирования.
    """
    
    def __init__(self):
        self._users = [
            User(1, "Анна Сидорова", "anna@example.com", datetime(2024, 1, 15)),
            User(2, "Сергей Кузнецов", "sergey@example.com", datetime(2024, 1, 16)),
            User(3, "Мария Петрова", "maria@example.com", datetime(2024, 1, 17))
        ]
        self._counter = 4  # Счетчик для новых ID
    
    def get_all_users(self) -> List[User]:
        print("[MOCK DB] SELECT * FROM users")
        return self._users.copy()
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        print(f"[MOCK DB] SELECT * FROM users WHERE id = {user_id}")
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def add_user(self, name: str, email: str) -> User:
        print(f"[MOCK DB] INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
        new_user = User(self._counter, name, email)
        self._users.append(new_user)
        self._counter += 1
        return new_user
    
    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        print(f"[MOCK DB] UPDATE users SET {kwargs} WHERE id = {user_id}")
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
        return user
    
    def delete_user(self, user_id: int) -> bool:
        print(f"[MOCK DB] DELETE FROM users WHERE id = {user_id}")
        initial_count = len(self._users)
        self._users = [user for user in self._users if user.id != user_id]
        return len(self._users) < initial_count
    
    def search_users(self, query: str) -> List[User]:
        print(f"[MOCK DB] Поиск пользователей: {query}")
        query = query.lower()
        return [
            user for user in self._users
            if query in user.name.lower() or query in user.email.lower()
        ]

if __name__ == "__main__":
    # Создаем заглушку базы данных
    db = MockDatabase()
    
    print("Все пользователи:")
    for user in db.get_all_users():
        print(f"  - {user.name} ({user.email})")
    
    print("\nПоиск 'иванов':")
    found_users = db.search_users("иванов")
    for user in found_users:
        print(f"  - {user.name}")
    
    new_user = db.add_user("Иван Иванов", "ivan@test.com")
    print(f"\nДобавлен новый пользователь: {new_user.name}")
    
    user = db.get_user_by_id(1)
    if user:
        print(f"\nПользователь с ID 1: {user.name}")
