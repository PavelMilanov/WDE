from typing import List, Dict
from pydantic import BaseModel, Field
from datetime import date


class Template(BaseModel):
    id: int
    filename: str
    url: str


class TemplateContext(Template):
    context: List[str]


class CreateDocument(BaseModel):
    id: int = Field(default=1, description='Id Template.')
    url: str = Field(default='forms/template.docx', description='Path to the template file.')
    context: Dict[str, str] = Field(description="Context to the template file.")


class RegistrationUser(BaseModel):
    id: int | None
    login: str = Field(default='login', description='User login name.')
    password: str = Field(default='password', description='user password.')


class GetToken(BaseModel):
    registration_id: int
    token: str
    expired_date: date
