from typing import List
from fastapi import APIRouter, UploadFile, status
from fastapi.responses import FileResponse
from services.fileeditor import FileEditor
from services.database import db
from models.models import TemplateContext, Template


router = APIRouter(
    prefix='/api/templates',
    tags=['templates']
)


@router.post("/upload/")
async def upload_template_file(file: UploadFile) -> status:
    """Загрузка файла на сервер.

    Args:
        file (UploadFile): fastapi.UploadFile (файл пользователя).

    Returns:
        status: успешно - 201, файл уже существует - 402.
    """      
    file, url = await FileEditor.upload_file(filename=file.filename, content=file.file)
    if file and url:
        await db.insert_template(file, url)
        return status.HTTP_201_CREATED
    return status.HTTP_402_PAYMENT_REQUIRED
    
@router.post('/download/{id}')
async def download_template(id: int)-> FileResponse:
    """Выгрузка файла пользователю.

    Args:
        id (int): id schemas.postgres.Template.

    Returns:
        FileResponse: fastapi.responses.FileResponce.
    """    
    model = await db.get_template(id)
    return FileResponse(
        path=model.url,
        filename='template.docx',
        media_type='application/octet-stream'
    )

@router.get('/')
async def get_templates() -> List[Template]:
    """Возвращает все шаблоны.

    Returns:
        List[Template]: schemas.postgres.Template.
    """
    return await db.get_templates()

@router.get('/{id}')
async def get_template(id: int) -> TemplateContext:
    """Возвращает шаблон с тегами, которые изменяются.

    Args:
        id (int): id schemas.postgres.Template.

    Returns:
        TemplateContext: models.model.TemplateContext.
    """
    model = await db.get_template(id)
    context = await FileEditor.get_context_file(model.url)
    return TemplateContext(
        id=model.id,
        filename=model.filename,
        url=model.url,
        context=context
    )
