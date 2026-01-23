from datetime import datetime
from typing import List, Optional, Dict

fake_db = [
    {
        "id": 1,
        "name": "Asier",
        "email": "asier@email.com",
        "password": "$2b$12$...",
        "role": "user",
        "created_at": datetime.utcnow(),
    },
    {
        "id": 2,
        "name": "Paco",
        "email": "paco@email.com",
        "password": "$2b$12$zC7F6gDMg..r9rXN4aTBu.nHXYWr/UhiSZikOODcH8S2zUoree/12",
        "role": "user",
        "created_at": datetime.utcnow(),
    },
    {
        "id": 3,
        "name": "Nora",
        "email": "nora@email.com",
        "password": "$2y$10$ucFHdCarBdDm0md0K0xg5.ZO5SU8Z3CjZYzSOta7jQ2d352lfE4Ri",
        "role": "admin",
        "created_at": datetime.utcnow(),
    }
]

def add_user(user_dict: Dict) -> Dict:
    fake_db.append(user_dict)
    return user_dict

def get_all_users() -> List[Dict]:
    return fake_db

def get_user_by_email(email:str) -> Optional[Dict]:
    for user in fake_db:
        if user["email"] == email:
            return user
    return None

def get_user_by_id(id: int):
    for user in fake_db:
        if user['id'] == id:
            return user
    return None