from pydantic import BaseModel

class ClientIn(BaseModel):
    clientId: int

class ClientOut(BaseModel):
    clientId: int
    name: str
    cat: str

    class Config:
        orm_mode = True

class NewClient(BaseModel):
    clientId: int
    name: str