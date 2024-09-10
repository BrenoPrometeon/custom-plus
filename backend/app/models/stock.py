from datetime import date
from graphemy import Field, Graphemy, Dl

class Stock(Graphemy, table=True):
    product_id: int | None = Field(primary_key=True, default=None)
    quantity: int
    last_price: float
    total: float