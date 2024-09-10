from datetime import date
from graphemy import Field, Graphemy, Dl

class Order(Graphemy, table=True):
    id: int | None = Field(primary_key=True, default=None)
    product_id: int 
    client_id: int
    payment: str | None
    order_date: date
    delivery_date: date | None
    quantity: int 
    discount: int | None
    
    products: list["Product"] = Dl(
        source="product_id", target="id"
    )