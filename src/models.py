import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    last_name = Column(String(10), nullable=False)
    password = Column(String(10), nullable=False)
    email = Column(String, nullable=False)
    
    favoritos = relationship('Favorito', back_populates='usuario')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email,
        }
    

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    height = Column(String)
    gender = Column(String)
    mass = Column(String)

    favoritos = relationship('Favorito', back_populates='personaje')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
            "mass": self.mass,
        }

class Planeta(Base):
    __tablename__= 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    climate = Column(String)
    terrain = Column(String)
    population = Column(String)

    favoritos = relationship('Favorito', back_populates='planeta')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
        }


class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    length = Column(String)
    crew = Column(String)
    passengers = Column(String)

    favoritos = relationship('Favorito', back_populates='vehiculo')

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
        }


class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'),nullable=False)
    personaje_id = Column(Integer, ForeignKey('personajes.id'), nullable=True )
    planeta_id = Column(Integer, ForeignKey('planetas.id'), nullable=True )
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id'), nullable=True )

    usuario = relationship('Usuario', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    vehiculo = relationship('Vehiculo', back_populates='favoritos')

    def to_dict(self):
        return{
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id,
            "vehiculo_id": self.vehiculo_id,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
