from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Template(Base):
    __tablename__ = 'templates'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    url = Column(String(20), unique=True, nullable=False)
