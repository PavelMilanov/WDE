from passlib.context import CryptContext
from .database import db


class Authentification:
    
    pwd_schema = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def registration_user(self, login: str, password: str) -> bool:
        """Функция регистрации пользователя по логину и паролю.

        Args:
            login (str): логин (application/x-www-form-urlencoded).
            password (str): пароль (application/x-www-form-urlencoded).

        Returns:
            bool: статус.
        """        
        hash_password = self.pwd_schema.hash(password)
        if await db.insert_registration(login, hash_password):
            return True
    
    async def authentification_user(self, login: str, password: str) -> bool:
        model = await db.select_registration(login)
        if self.pwd_schema.verify(password, model.password):
            return True


auth = Authentification()
