from fastapi import APIRouter, UploadFile, status
from services.fileeditor import FileEditor


router = APIRouter(
    prefix='/api/templates',
    tags=['web']
)


@router.post("/upload/")
async def upload_template_file(file: UploadFile) -> status:
    """Загружает шаблон на сервер.
    
    file: загружаемый файл.
    
    return: при успешной загрузке - status 201
            если файл уже существует - status 404
    """
    file_saved = await FileEditor.upload_file(filename=file.filename, content=file.file)
    return status.HTTP_201_CREATED if file_saved else status.HTTP_404_NOT_FOUND