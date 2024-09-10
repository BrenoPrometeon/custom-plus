import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graphemy import Graphemy, GraphemyRouter, import_files
from .models import *

from .dependencies import engine, settings


import_files(os.path.dirname(__file__))

Graphemy.metadata.create_all(engine)

app = FastAPI()

router = GraphemyRouter(
    engine=engine, enable_put_mutations=True, enable_delete_mutations=True
)

app.include_router(router, prefix="/graphql")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## READ

@app.get("/")
async def read_indicator():
    print('Hello World')
    return None