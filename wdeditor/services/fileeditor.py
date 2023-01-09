import shutil, os
from typing import BinaryIO, Set
from docxtpl import DocxTemplate
from . import template_path, doc_path
from models import models
from datetime import date


class FileEditor:
    
    @staticmethod
    async def upload_file(filename: str, content: BinaryIO) -> str:
        if not os.path.exists(f'{template_path}/{filename}'):
            with open(f'{template_path}/{filename}', "wb") as wf:
                shutil.copyfileobj(content, wf)
                content.close()
            url = f'{template_path}/{filename}'
            return filename, url

    @staticmethod
    async def get_context_file(file_path: str) -> Set[str]:
        doc = DocxTemplate(file_path)
        return doc.get_undeclared_template_variables()

    @staticmethod
    async def delete_file(file_path: str) -> Exception:
        try:
            os.remove(file_path)
        except Exception as e:
            return e
    
    @staticmethod
    async def generate_document_by_template(data: models.CreateDocument ) -> str:
        doc = DocxTemplate(data.url)
        context = data.context
        filename = date.today().strftime("%d.%m.%Y")
        doc.render(context)
        doc.save(f'{doc_path}/{filename}.docx')
        return f'{doc_path}/{filename}.docx'
