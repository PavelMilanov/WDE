from typing import List
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session
from schemas.postgres import *
from models import models


class PostgresApi:


    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = create_engine(self.db_url, echo=True, future=True)

    async def insert_template(self, filename: str, url: str):
        """Создает запись в таблице templates.

        Args:
            filename (str): навзвание файла.
            url (str): относительный url файла.
        """        
        with Session(self.engine) as session:
            new_template = Template()
            new_template.name = filename
            new_template.url = url
            session.add(new_template)
            try:
                session.commit()
            except Exception:
                session.rollback()

    async def get_templates(self) -> List[Template]:
        """Возвращает список всех шаблонов.

        Returns:
            List[Template]: список моделей Template.
        """        
        with Session(self.engine) as session:
            object = session.query(Template).all()
        return object

    async def get_template(self, id: int) -> models.Template:
        """Возврашает шаблон.

        Args:
            id (int): id шаблона.

        Returns:
            models.Template: модель Template.
        """        
        with Session(self.engine) as session:
            object = session.query(Template).where(Template.id == id).first()
            return models.Template(
                id=object.id,
                filename=object.name,
                url=object.url
            )

    async def delete_template(self, id: int) -> models.Template:
        """Удалеят шаблон.

        Args:
            id (int): id шаблона.

        Returns:
            models.Template: _description_
        """        
        with Session(self.engine) as session:
            object = session.query(Template).where(Template.id == id).first()
            session.delete(object)
            try:
                session.commit()
                return models.Template(
                    id=object.id,
                    filename=object.name,
                    url=object.url
                )
            except Exception:
                session.rollback()
    
    async def insert_registration(self, login: str, password: str):
        with Session(self.engine) as session:
            new_registration = Registration()
            new_registration.login = login
            new_registration.password = password
            session.add(new_registration)
            try:
                session.commit()
            except Exception:
                session.rollback()
    
    async def select_registration(self, login: str, password: str):
        with Session(self.engine) as session:
            object = session.query(Registration).where(and_(Registration.login == login, Registration.password == password)).first()
            return models.Template(
                id=object.id,
                filename=object.name,
                url=object.url
            )

db = PostgresApi('postgresql://postgres:admin@localhost:5432/postgres')
