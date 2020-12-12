from typing import Dict
from pydantic import BaseModel
class ClientInDB(BaseModel):
    clientId: int
    name: str
    cat: str     # Categotía del cliente segun antigüedad

database_clients = Dict[int, ClientInDB]
database_clients = {
    2840910: ClientInDB(**{"clientId":2840910,
                            "name":"Antonio Uribe",
                            "cat":"B"}),
    1014892339: ClientInDB(**{"clientId":1014892339,
                            "name":"Melissa Camacho",
                            "cat":"A"}),
}

#generator = {"id":2}

def save_client(client_in_db: ClientInDB):
    #generator["id"] = generator["id"] + 1
    #reserva_in_db.id_reserva = generator["id"]
    database_clients[client_in_db.clientId] = client_in_db              #.append(reserva_in_db)
    return client_in_db

def get_client(clientId: int):
    if clientId in database_clients.keys():
        return database_clients[clientId]
    else:
        return None

def update_client(client_in_db: ClientInDB):
    database_clients[client_in_db.clientId] = client_in_db
    return client_in_db