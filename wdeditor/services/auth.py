from passlib.context import CryptContext
from jose import jwt
from .database import db


class Authentification:
    
    
    pwd_schema = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def registration_user(self, login: str, password: str):
        hash_password = self.pwd_schema.hash(password)
        await db.insert_registration(login, hash_password)
    
    async def authentification_user(self, login: str, password: str):
        pass