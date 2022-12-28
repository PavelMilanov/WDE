from fastapi import APIRouter


router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)


@router.post('/authentificate')
async def authentificate_user():
    pass

@router.post('/registration')
async def register_user():
    pass
