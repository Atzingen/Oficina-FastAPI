from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, \
                       String, Float, DateTime
from sqlalchemy.orm import relationship

from config import Base


class Sensor(Base):
    __tablename__ = 'sensores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    grandeza_fisica = Column(String(50))
    image_url = Column(String(200))
    datasheet_url = Column(String(200))

    dados = relationship("Dado", back_populates="sensores")

    def __repr__(self):
        return f"<Sensor(id={self.id}, nome={self.nome}, grandeza_fisica={self.grandeza_fisica})>"


class Dado(Base):
    __tablename__ = 'dados'

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    tempo = Column(DateTime)
    sensor_id = Column(Integer, ForeignKey('sensores.id'))

    sensores = relationship("Sensor", back_populates="dados")

    def __repr__(self):
        return f"<Dado(id={self.id}, valor={self.valor}, tempo={self.tempo}, sensor_id={self.sensor_id})>"