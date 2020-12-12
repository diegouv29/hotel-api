from datetime import datetime
from pydantic import BaseModel

class ReservaInDB(BaseModel):
    id_reserva: int = 0
    clientId: int
    check_in: str
    check_out: str
    dias: int
    valor: int

database_reservas = []
generator = {"id":0}

def save_reserva(reserva_in_db: ReservaInDB):
    generator["id"] = generator["id"] + 1
    reserva_in_db.id_reserva = generator["id"]
    database_reservas.append(reserva_in_db)
    return reserva_in_db
