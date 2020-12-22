from pydantic import BaseModel

class ReservaIn(BaseModel):
    clientId: int
    check_in: str
    check_out: str
    habit: int

class ReservaOut(BaseModel):
    id_reserva: int
    clientId: int
    check_in: str
    check_out: str
    habit: int
    dias: int
    valor: int

    class Config:
        orm_mode = True