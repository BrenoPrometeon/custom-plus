from graphemy import Field, Graphemy, Dl


class Customer(Graphemy, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str
    phone: str
    address: str | None
    email: str | None