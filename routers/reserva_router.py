from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.cliente_db import ClientInDB
from db.reserva_db import ReservaInDB

from models.cliente_models import ClientIn, ClientOut, NewClient
from models.reserva_models import ReservaIn, ReservaOut

from datetime import datetime

router = APIRouter()

@router.put("/client/reserva/", response_model=ReservaOut)
async def make_reserva(reserva_in: ReservaIn,
                            db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(reserva_in.clientId)

    if client_in_db == None:
        raise HTTPException(status_code=404,
                            detail="Cliente no creado")

    date_in = datetime.strptime(reserva_in.check_in, '%Y-%m-%d')
    date_out = datetime.strptime(reserva_in.check_out, '%Y-%m-%d')

    if date_out <= date_in:
        raise HTTPException(status_code=400,
            detail="La fecha de salida debe ser posterior a la de entrada")

    cant_dias = date_out - date_in
    num_dias = int(cant_dias.days)
    cost = num_dias*80000

    db.commit()
    db.refresh(client_in_db)

    reserva_in_db = ReservaInDB(**reserva_in.dict(), dias = num_dias, valor = cost)

    db.add(reserva_in_db)
    db.commit()
    db.refresh(reserva_in_db)

    return reserva_in_db