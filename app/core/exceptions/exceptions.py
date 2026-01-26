# Aquí van todos los tipos de excepciones que pueden ocurrir en la aplicación

class UserNotFound(Exception):
    def __init__(self, user_id: int | None = None, username: str = None):
        self.user_id = user_id
        self.username = username
        super().__init__("User not found")

class UserAlreadyExists(Exception):
    def __init__(self, user_id: int | None = None, username: str = None):
        self.user_id = user_id
        self.username = username
        super().__init__("User already exists")