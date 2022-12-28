from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers import templates, documents, auth
from services.fileeditor import FileEditor


app = FastAPI(
    title='WDE API',
    description='Rest-API',
    version='0.1.0',
    prefix='/api/'
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
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    # 
    return response