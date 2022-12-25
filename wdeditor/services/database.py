from typing import List
from sqlalchemy import create_engine, select
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
        with Session(self.engine) as session:
            req = select(Template)
            data = session.execute(req).scalars().all()
        return data
    
    async def get_template(self, id: int) -> models.Template:
        with Session(self.engine) as session:
            req = select(Template).where(Template.id == id)
            data = session.execute(req).scalars().first()
        return models.Template(
            id=data.id,
            filename=data.name,
            url=data.url
        )


db = PostgresApi('postgresql://postgres:admin@localhost:5432/postgres')
