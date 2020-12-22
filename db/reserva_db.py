from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, DateTime
import datetime
from db.db_connection import Base, engine

class ReservaInDB(Base):
    __tablename__ = "reservas"

    id_reserva = Column(Integer, primary_key=True, autoincrement=True)
    clientId = Column(Integer, ForeignKey("clients.clientId"))
    check_in = Column(String)
    check_out = Column(String)
    habit = Column(Integer)
    dias = Column(Integer)
    valor = Column(Integer)

Base.metadata.create_all(bind=engine)

