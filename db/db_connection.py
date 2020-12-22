from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Noviembre29@localhost:5432/MISIONTIC"
engine = create_engine(DATABASE_URL)

#Creacion de la sesion.
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Base para la creacion de los modelos
Base = declarative_base()
Base.metadata.schema = "hoteldb"