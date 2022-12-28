from typing import List
from fastapi import APIRouter, UploadFile, status, Path
from fastapi.responses import FileResponse
from services.fileeditor import FileEditor
from services.database import db
from models.models import TemplateContext, Template


router = APIRouter(
    prefix='/api/templates',
    tags=['templates']
)


@router.post("/upload")
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
async def download_template(id: int = Path(default=1, alias='Id Template', description='Id Template', example='/download/1'))-> FileResponse:
    """Выгрузка файла пользователю.

    Args:
        id (int): id шаблона.

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
        List[Template]: модели шаблона.
    """
    return await db.get_templates()

@router.get('/{id}')
async def get_template(id: int = Path(default=1, description='Id Template', example='1')) -> TemplateContext:
    """Возвращает шаблон с тегами, которые изменяются.

    Args:
        id (int): id шаблона.

    Returns:
        TemplateContext: модель шаблона с тегами.
    """
    model = await db.get_template(id)
    context = await FileEditor.get_context_file(model.url)
    return TemplateContext(
        id=model.id,
        filename=model.filename,
        url=model.url,
        context=context
    )

@router.delete('/{id}')
async def delete_template(id: int = Path(default=1, alias='Id Template', description='Id Template', example='/delete/1')) -> int:
    """Удаляет шаблон.

    Args:
        id (int): id шаблона.

    Returns:
        int: успешно - if шаблона, не успешно - 403 статус.
    """    
    model = await db.delete_template(id)
    err = await FileEditor.delete_file(model.url)
    return model.id if not err else status.HTTP_403_FORBIDDEN
