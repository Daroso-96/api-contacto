from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost:5432/agenda'
def conectar():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    s = Session()

    if s != None:
        print("Conexion exitosa")
    else:
        print("Error conexion")

    return s