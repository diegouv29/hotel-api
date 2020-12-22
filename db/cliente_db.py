from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine

class ClientInDB(Base):
    __tablename__ = "clients"

    clientId = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    cat = Column(String)

Base.metadata.create_all(bind=engine)
