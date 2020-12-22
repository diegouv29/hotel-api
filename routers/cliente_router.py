from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.cliente_db import ClientInDB
from db.reserva_db import ReservaInDB

from models.cliente_models import ClientIn, ClientOut, NewClient
from models.reserva_models import ReservaIn, ReservaOut

router = APIRouter()

@router.post("/client/new/")
async def in_client(new_client: NewClient, db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(new_client.clientId)

    if client_in_db != None:
        raise HTTPException(status_code=404,
                            detail="El cliente ya existe")

    client_in_db = ClientInDB(**new_client.dict(), cat = "C")

    db.add(client_in_db)
    db.commit()
    db.refresh(client_in_db)

    return client_in_db


@router.get("/client/info/{clientId}", response_model=ClientOut)
async def get_info(clientId: int, db: Session = Depends(get_db)):
    client_in_db = db.query(ClientInDB).get(clientId)

    if client_in_db == None:
        raise HTTPException(status_code=404,
                            detail="Cliente no creado")

    return client_in_db


