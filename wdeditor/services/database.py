from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from schemas import postgres
from models import models
from datetime import date


class PostgresApi:


    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url, echo=True, future=True)

    async def insert_template(self, filename: str, url: str) -> bool | Exception:
        """Создает запись в таблице templates.

        Args:
            filename (str): навзвание файла.
            url (str): относительный url файла.
            
        Returns:
            bool | Exception: успешно | неуспешно.
        """        
        with Session(self.engine) as session:
            new_template = postgres.Template()
            new_template.name = filename
            new_template.url = url
            session.add(new_template)
            try:
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                return e

    async def get_templates(self) -> List[postgres.Template]:
        """Возвращает список всех шаблонов.

        Returns:
            List[Template]: список моделей Template.
        """        
        with Session(self.engine) as session:
            object = session.query(postgres.Template).all()
        return object

    async def get_template(self, id: int) -> models.Template:
        """Возврашает шаблон.

        Args:
            id (int): id шаблона.

        Returns:
            models.Template: модель Template.
        """        
        with Session(self.engine) as session:
            object = session.query(postgres.Template).where(postgres.Template.id == id).first()  # noqa: E501
            return models.Template(
                id=object.id,
                filename=object.name,
                url=object.url
            )

    async def delete_template(self, id: int) -> models.Template | Exception:
        """Удалеят шаблон.

        Args:
            id (int): id шаблона.

        Returns:
            models.Template | Exception: успешно | неуспешно.
        """        
        with Session(self.engine) as session:
            object = session.query(postgres.Template).where(postgres.Template.id == id).first()  # noqa: E501
            session.delete(object)
            try:
                session.commit()
                return models.Template(
                    id=object.id,
                    filename=object.name,
                    url=object.url
                )
            except Exception as e:
                session.rollback()
                return e
    
    async def insert_registration(self, login: str, password: str) -> bool | Exception:
        """Создает запись в таблице registratioons. 

        Args:
            login (str): логин.
            password (str): пароль.

        Returns:
            bool | Exception: успешно | неуспешно.
        """        
        with Session(self.engine) as session:
            new_registration = postgres.Registration()
            new_registration.login = login
            new_registration.password = password
            session.add(new_registration)
            try:
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                return e
    
    async def select_registration(self, login: str) -> models.RegistrationUser:
        """Возвращает id, логин, пароль по совпадению "login".

        Args:
            login (str): логин.

        Returns:
            models.RegistrationUser: id, логин, пароль.
        """        
        with Session(self.engine) as session:
            object = session.query(postgres.Registration).where(postgres.Registration.login == login).first()  # noqa: E501
            if object is not None:
                return models.RegistrationUser(
                    id=object.id,
                    login=object.login,
                    password=object.password
                )

    async def insert_token(self, registrationid: int, token: str, expired_date: date):
        with Session(self.engine) as session:
            new_token = postgres.Token()
            new_token.registration_id = registrationid
            new_token.token = token
            new_token.expire_of = expired_date
            session.add(new_token)
            try:
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                return e
    
    async def select_token(self, registrationid: int):
        with Session(self.engine) as session:
            object = session.query(postgres.Token).where(postgres.Token.registration_id == registrationid).first()  # noqa: E501
            if object is not None:
                return models.GetToken(
                    registration_id=object.registration_id,
                    token=object.token,
                    expired_date=object.expire_of
                )
    
    async def delete_token(self, registrationid: int):
        with Session(self.engine) as session:
            object = session.query(postgres.Token).where(postgres.Token.registration_id == registrationid).first()  # noqa: E501
            session.delete(object)
            try:
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                return e

db = PostgresApi('postgresql://postgres:admin@localhost:5432/postgres')
