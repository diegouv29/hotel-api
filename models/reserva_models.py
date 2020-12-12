from pydantic import BaseModel
from datetime import datetime

class ReservaIn(BaseModel):
    clientId: int
    check_in: str
    check_out: str

class ReservaOut(BaseModel):
    id_reserva: int
    clientId: int
    check_in: str
    check_out: str
    dias: int
    valor = int