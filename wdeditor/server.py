from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.web import web


app = FastAPI(
    title='WDE API',
    description='Rest-API',
    version='0.1.0',
    prefix='/api/'
)

app.include_router(web.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'DELETE'],
    allow_headers=['*'],
)