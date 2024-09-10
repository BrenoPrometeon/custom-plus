from datetime import date
from graphemy import Field, Graphemy, Dl


class Supplier(Graphemy, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str
    address: str | None
    cnpj: str | None
    contact: str