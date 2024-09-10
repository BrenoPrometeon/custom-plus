from datetime import date
from graphemy import Field, Graphemy, Dl

class Product(Graphemy, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str 
    description: str | None
    category: str | None