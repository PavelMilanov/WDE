from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

auth_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/authentificate')


@router.post('/authentificate')
async def authentificate_user(form: OAuth2PasswordRequestForm = Depends()):
    login, password = form.username, form.password
    return login, password

@router.post('/registration')
async def register_user():
    pass
