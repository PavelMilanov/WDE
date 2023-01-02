from passlib.context import CryptContext
from jose import jwt
from .database import db
from datetime import date, datetime

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
    
    async def authentification_user(self, login: str, password: str) -> str| None:
        model = await db.select_registration(login)
        if self.pwd_schema.verify(password, model.password):
            token = await self.__generate_token(model.id)
            return token

    async def __generate_token(self, registrationid: int):
        expired_date = await self.__expired_date()
        token = jwt.encode({'expired': str(expired_date), 'userid': str(registrationid)}, 'secret', algorithm='HS256')
        check = await db.insert_token(registrationid, token, expired_date)
        if not isinstance(check, Exception): 
            return token
        else:
            print(check)
    
    async def __expired_date(self):
        current_date = datetime.now()
        return date(current_date.year, current_date.month, current_date.day+2)
    

auth = Authentification()
