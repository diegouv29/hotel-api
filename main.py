from fastapi import Depends, FastAPI
from routers.cliente_router import router as router_clients
from routers.reserva_router import router as router_reservas
api = FastAPI()
api.include_router(router_clients)
api.include_router(router_reservas)
