from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Template(Base):
    __tablename__ = 'templates'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    url = Column(String(20), unique=True, nullable=False)


class Registration(Base):
    __tablename__ = 'registrations'
    
    user_id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True, nullable=False)
    password = Column(String(255), unique=True, nullable=False)
