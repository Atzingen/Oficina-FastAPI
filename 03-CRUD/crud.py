from typing import List
from datetime import datetime
from config import SessionLocal, engine
import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_sensor(db: SessionLocal,
               sensor_id: int,
               qt: int = 1):
    return db.query(models.Dado).\
              filter(models.Dado.sensor_id == sensor_id).\
              order_by(models.Dado.tempo.desc()).\
              limit(qt).all()

def insert_sensor_data(db: SessionLocal,
                  sensor_id: int,
                  sensor_values: List[float]):
    dados = []
    print(sensor_id, sensor_values)
    for sensor_value in sensor_values:
        dados.append(models.Dado(valor=sensor_value, 
                        tempo=datetime.now(), 
                        sensor_id=sensor_id))
    db.add_all(dados)
    response = db.commit()