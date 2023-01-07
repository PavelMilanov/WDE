from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from services.auth import auth
from models import models


router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

auth_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/authentificate')


async def is_active_user(token: str = Depends(auth_scheme)):
    await auth.is_active_user(token)

@router.post('/registration')
async def register_user(registration_form: models.RegistrationUser = Body(embed=True)):
    registration = await auth.registration_user(registration_form.login, registration_form.password)
    return registration

@router.post('/authentificate')
async def authentificate_user(form: OAuth2PasswordRequestForm = Depends()):
    token = await auth.authentification_user(form.username, form.password)
    if token:
        return {
            "access_token": token,
            "token_type": "bearer"
            }
    else:
        return 'авторизация не пройдена'

@router.get('/me')
async def test(token: str = Depends(is_active_user)):
    return 'hello world'