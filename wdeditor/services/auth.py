from passlib.context import CryptContext
from jose import jwt
from .database import db
from datetime import date
from typing import Final


class Authentification:
    
    pwd_schema = CryptContext(schemes=["bcrypt"], deprecated="auto")
    ALGORITHM: Final = 'HS256'
    SECRET: Final = 'secret'

    async def registration_user(self, login: str, password: str) -> bool:
        """Функция регистрации пользователя по логину и паролю.

        Args:
            login (str): логин (application/x-www-form-urlencoded).
            password (str): пароль (application/x-www-form-urlencoded).

        Returns:
            bool: статус.
        """
        check_user = await db.select_registration(login)
        if check_user:
            return f'пользователь {check_user.login} уже существует'
        else:          
            hash_password = self.pwd_schema.hash(password)
            if await db.insert_registration(login, hash_password):
                return 'успешная регистрация'
            else:
                return 'что-то пошло нетак'
    
    async def authentification_user(self, login: str, password: str) -> str | None:
        model = await db.select_registration(login)
        if model is not None:  # если запись о регистрации есть
            if self.pwd_schema.verify(password, model.password):  # если прошла проверка, пробуем получить токен
                token = await self.__get_token(model.id)
                if token is None:  # если токена нет, создаем новый
                    new_token = await self.__generate_token(model.id)
                    return new_token
                return token.token
    
    async def is_active_user(self, token):
        d_token = jwt.decode(token, self.SECRET, algorithms=[self.ALGORITHM])
        model = await self.__get_token(int(d_token['userid']))
        if model.expired_date < date.today():
            await db.delete_token(model.registration_id)
             
    async def __generate_token(self, registrationid: int):
        expired_date = await self.__expired_date()
        token = jwt.encode({'userid': str(registrationid)}, self.SECRET, algorithm=self.ALGORITHM)
        check = await db.insert_token(registrationid, token, expired_date)
        if not isinstance(check, Exception): 
            return token
        else:
            print(check)
    
    async def __get_token(self, registrationid: int):
        model = await db.select_token(registrationid)
        return model
    
    async def __expired_date(self):
        current_date = date.today()
        return date(current_date.year, current_date.month, current_date.day+2)
    

auth = Authentification()
