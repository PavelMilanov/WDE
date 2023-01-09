import re
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers import templates, documents, auth


description = """
Rest-API
"""


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Операции с регистрацией и авторизацией пользователей.'
    },
    {
        'name': 'templates',
        'description': 'Операции с шаблонами документов.'
    },
    {
        'name': 'documents',
        'description': 'Операции с документами.'
    },
] 

app = FastAPI(
    title='WDE API',
    description=description,
    version='0.1.0',
    prefix='/api/',
    openapi_url='/api/openapi.json',
    docs_url='/api/docs',
    redoc_url=None,
    openapi_tags=tags_metadata,
    contact={
        'name': 'Pavel Milanov',
        'url': 'https://github.com/PavelMilanov',
        'email': 'pawel.milanov@yandex.ru'
    }
)

app.include_router(auth.router)
app.include_router(templates.router)
app.include_router(documents.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'DELETE'],
    allow_headers=['*'],
)

@app.middleware("http")
async def remove_tmp_file(request: Request, call_next):
    response = await call_next(request)
    url = request.headers.get('referer')
    try:
        search = re.search(r'.docx', url)
        if search:
            print(search)
    except TypeError as e:
        print(e)

    return response
