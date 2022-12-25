import shutil, os
from typing import BinaryIO, Set
from docxtpl import DocxTemplate
from . import template_path


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
