from typing import List
from pydantic import BaseModel


class Template(BaseModel):
    id: int
    filename: str
    url: str


class TemplateContext(Template):
    context: List[str]
