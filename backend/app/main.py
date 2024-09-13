import os
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, SQLModel, create_engine, select
from graphemy import Graphemy, GraphemyRouter, import_files
from .models.customer import Customer
from .models.order import Order
from .models.product import Product
from .models.purchases import Purchases
from .models.stock import Stock
from .models.supplier import Supplier

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

@app.get("/customer/")
async def read_customer():
    with Session(engine) as session:
        indicator = session.exec(select(Customer)).all()
        return indicator

@app.get("/order/")
async def read_order():
    with Session(engine) as session:
        indicator = session.exec(select(Order)).all()
        return indicator

@app.get("/product/")
async def read_product():
    with Session(engine) as session:
        indicator = session.exec(select(Product)).all()
        return indicator

@app.get("/purchase/")
async def read_purchase():
    with Session(engine) as session:
        indicator = session.exec(select(Purchases)).all()
        return indicator

@app.get("/stock/")
async def read_stock():
    with Session(engine) as session:
        indicator = session.exec(select(Stock)).all()
        return indicator

@app.get("/supplier/")
async def read_supplier():
    with Session(engine) as session:
        indicator = session.exec(select(Supplier)).all()
        return indicator