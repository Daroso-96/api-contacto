import dataclasses
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass
Base = declarative_base()

@dataclass
class Usuario(Base):
    id: int
    nombre: str
    apellidos: str
    email:str
    password:str

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellidos = Column(String)
    email = Column(String)
    password= Column(String)
    def __repr__(self):
        return f"<Usuario(id={self.id},nombre={self.nombre},apellidos={self.apellidos},email={self.email}, password={self.password}"

@dataclass
class Contacto(Base):
    id:int
    nombre:str
    apellidos:str
    direccion:str
    email:str
    telefono:str
    fechaCreacion:datetime

    __tablename__ = 'contacto'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    fechaCreacion= Column(DateTime, default=datetime.today())

    def __repr__(self):
        return f"<Contacto(id={self.id},nombre={self.nombre},apellidos={self.apellidos},direccion={self.direccion}, email={self.email}, telefono={self.telefono}, fechaCreacion={self.fechaCreacion}"

@dataclass
class Pertenece(Base):
    id: int
    id_usuario:int
    id_contacto:int
    __tablename__ = 'pertenece'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable= False)
    id_contacto = Column(Integer, nullable=False)