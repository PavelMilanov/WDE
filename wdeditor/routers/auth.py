from fastapi import APIRouter, Depends, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from services.auth import auth
from models import models


router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

auth_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/authentificate')


@router.post('/registration')
async def register_user(registration_form: models.RegistrationUser = Body(embed=True)):
    registration = await auth.registration_user(registration_form.login, registration_form.password)
    return registration

@router.post('/authentificate')
async def authentificate_user(form: OAuth2PasswordRequestForm = Depends()):
    token = await auth.authentification_user(form.username, form.password)
    if token:
        return token
    else:
        return 'авторизация не пройдена'
