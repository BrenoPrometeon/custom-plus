from datetime import date
from graphemy import Field, Graphemy, Dl


class Purchases(Graphemy, table=True):
    id: int | None = Field(primary_key=True, default=None)
    product_id: int 
    supplier_id: int
    quantity: int
    price: float
    payment_method: str | None
    purchase_date: date