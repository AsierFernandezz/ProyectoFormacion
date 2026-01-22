from datetime import datetime
from typing import List, Optional, Dict

fake_db: List[dict] = [{"id": 1, "name": "Paco", "email": "paco@gmail.com", "created_at": datetime.now(), "role": "user"}]

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
