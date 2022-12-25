from fastapi import APIRouter, UploadFile, status
from fastapi.responses import FileResponse
from services.fileeditor import FileEditor


router = APIRouter(
    prefix='/api/templates',
    tags=['templates']
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

@router.post('/download/{id}')
async def download_template(id: int):
    return FileResponse(
        'forms/form1.docx',
        filename='template.docx',
        media_type='application/octet-stream'
    )

@router.get('/')
async def get_templates():
    return

@router.get('/{id}')
async def get_template_params():
    return