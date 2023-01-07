from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship
 
 
Base = declarative_base()


class Template(Base):
    __tablename__ = 'templates'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    url = Column(String(20), unique=True, nullable=False)


class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True, nullable=False)
    password = Column(String(255), unique=True, nullable=False)
    user = relationship(
        'User',
        back_populates='registration',
        cascade='all,delete',
        passive_deletes=True
        )
    token = relationship(
        'Token',
        back_populates='registration',
        cascade='all,delete',
        passive_deletes=True
        )


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, ForeignKey('registrations.id', ondelete='CASCADE'), primary_key=True)
    name = Column(String(20))
    second_name = Column(String(20))
    surname = Column(String(20))
    registration = relationship(
        'Registration',
        back_populates='user'
        )


class Token(Base):
    __tablename__ = 'tokens'

    registration_id = Column(Integer, ForeignKey('registrations.id', ondelete='CASCADE'), primary_key=True)  # noqa: E501
    token = Column(String(255), unique=True)
    expire_of = Column(Date, nullable=False)
    registration = relationship(
        'Registration',
        back_populates='token'
        )
