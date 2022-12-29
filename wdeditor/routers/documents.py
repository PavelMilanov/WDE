from fastapi import APIRouter, Body, Query, Path, Depends
from fastapi.responses import FileResponse
from services.fileeditor import FileEditor
from models.models import  CreateDocument
from .auth import auth_scheme


router = APIRouter(
    prefix='/api/documents',
    tags=['documents']
)


@router.post('/generate')
async def generate_document(context: CreateDocument = Body(embed=True), token: str = Depends(auth_scheme)):
    docuent = await FileEditor.generate_document_by_template(context)
    return docuent

@router.post('/{file}')
async def action_to_document(
    file: str = Path(title='Document name', description='Document name', example='31.12.12 12:00.docx', regex='^[0-9]{2}.[0-9]{2}.[0-9]{4} [0-9]{2}:[0-9]{2}.docx'), 
    action: str = Query(default='print', alias='action', title='Action to Document', description="Action to Document", example='print', regex='^print$|^save$'),
    token: str = Depends(auth_scheme)
    ):
    if action == 'print':
        return 'print document'
    else:
        return FileResponse(
        path=f'tmp/{file}',
        filename='autogenerate_document.docx',
        media_type='application/octet-stream',
        status_code=200
    )
