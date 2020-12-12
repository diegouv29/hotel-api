from db.cliente_db import ClientInDB
from db.cliente_db import update_client, get_client, save_client
from db.reserva_db import ReservaInDB
from db.reserva_db import save_reserva
from models.cliente_models import ClientIn, ClientOut, NewClient
from models.reserva_models import ReservaIn, ReservaOut

from datetime import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/client/new/")
async def in_client(new_client: NewClient):
    client_in_db = get_client(new_client.clientId)
    if client_in_db != None:
        raise HTTPException(status_code=404,
            detail="El cliente ya existe")

    client_in_db = ClientInDB(**new_client.dict(), cat = "C")
    client_in_db = save_client(client_in_db)

    client_out = ClientOut(**client_in_db.dict())
    return client_out


@api.get("/client/info/{clientId}")
async def get_info(clientId: int):
    client_in_db = get_client(clientId)
    if client_in_db == None:
        raise HTTPException(status_code=404,
            detail="Cliente no creado")
    client_out = ClientOut(**client_in_db.dict())
    return client_out

@api.put("/client/reserva/")
async def make_reserva(reserva_in: ReservaIn):

    client_in_db = get_client(reserva_in.clientId)

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

    reserva_in_db = ReservaInDB(**reserva_in.dict(), dias = num_dias, valor = cost)
    reserva_in_db = save_reserva(reserva_in_db)

    reserva_out = ReservaOut(**reserva_in_db.dict())
    return reserva_out