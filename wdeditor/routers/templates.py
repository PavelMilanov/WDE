from typing import List
from fastapi import APIRouter, UploadFile, Response, Path, Depends
from fastapi.responses import FileResponse
from services.fileeditor import FileEditor
from services.database import db
from models.models import TemplateContext, Template
from .auth import is_active_user


router = APIRouter(
    prefix='/api/templates',
    tags=['templates']
)


@router.post("/upload")
async def upload_template_file(file: UploadFile, token: str = Depends(is_active_user))-> Response:
    """Загрузка файла на сервер.

    Args:
        file (UploadFile): fastapi.UploadFile (файл пользователя).

    Returns:
        Responce: 201, 402.
    """      
    file, url = await FileEditor.upload_file(filename=file.filename, content=file.file)
    if file and url:
        if await db.insert_template(file, url):
            return Response(
                content='Шаблон добавлен',
                status_code=201
            )
        else:
            return Response(
                content='Шаблон уже существует',
                status_code=402
            )
    
@router.post('/download/{id}')
async def download_template(
    id: int = Path(default=1, alias='Id Template', description='Id Template', example='/download/1'),
    token: str = Depends(is_active_user)
    )-> FileResponse:
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
        media_type='application/octet-stream',
        status_code=201
    )

@router.get('/')
async def get_templates(token: str = Depends(is_active_user)) -> List[Template]:
    """Возвращает все шаблоны.

    Returns:
        List[Template]: модели шаблона.
    """
    return await db.get_templates()

@router.get('/{id}')
async def get_template(
    id: int = Path(default=1, description='Id Template', example='1'),
    token: str = Depends(is_active_user)
    ) -> TemplateContext:
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
async def delete_template(
    id: int = Path(default=1, alias='Id Template', description='Id Template', example='/delete/1'),
    token: str = Depends(is_active_user)
    ) -> Response:
    """Удаляет шаблон.

    Args:
        id (int): id шаблона.

    Returns:
        int: 202, 402.
    """    
    model = await db.delete_template(id)
    if not isinstance(model, Exception):
        err = await FileEditor.delete_file(model.url)
        if not err:
            return Response(
            content='Шаблон удален успешно',
            status_code=202
        )
        else:
            return Response(
            content='Ошибка при удалении шаблона',
            status_code=402
        )
    return Response(
        content='Ошибка при удалении шаблона в базе данных',
        status_code=402
    )
