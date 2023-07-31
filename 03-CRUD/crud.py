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
    return db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()
