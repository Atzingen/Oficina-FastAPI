import random
from typing import List
from fastapi import FastAPI, Response, status, Depends, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from sqlalchemy.orm import Session

from config import SessionLocal, engine
from crud import *
import models


models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Demo API com FastAPI",
    version="1.0.0",
    description='''
       Demo API com FastAPI

       Oficina do projeto IF+EMPREENDEDOR, campus Piracicaba.

       2o semestre 2023
    ''',
    contact={
        'email': 'gustavo.von@ifsp.edu.br'
    }
)

@app.get("/", status_code=status.HTTP_201_CREATED)
def home():
    return "home sweet home !!!"

@app.get("/dashboard/")
def dashboard(request: Request, db: Session = Depends(get_db)):
    a = get_sensor(db, 1, 1)
    t = get_sensor(db, 2, 7)
    t = [t.valor for t in t[:7]]
    print(t)
    return templates.TemplateResponse(
        'index.html',
        {
            "request": request,
            'a': a[0].valor,
            'b': 2,
            'temperaturas': t
        }
    )

@app.get("/read_sensor/")
def read_sensor(sensor_id: int = 1, 
                qt: int = 1,
                db: Session = Depends(get_db)):
    return get_sensor(db, sensor_id, qt)

@app.post("/insert_sensores")
def insert_sensor_post(sensor_id: int,
                       values: List[int],
                       db: Session = Depends(get_db)):
    insert_sensor_data(db, sensor_id, values)
    return status.HTTP_202_ACCEPTED

@app.get("/insert_sensor/{sensor_id}/{sensor_value}")
def insert_sensor(sensor_id: int, 
           sensor_value: float,
           db: Session = Depends(get_db)):
    resposta = insert_sensor_data(db, sensor_id, [sensor_value])
    return status.HTTP_202_ACCEPTED

if __name__ == '__main__':
    uvicorn.run('main:app', 
                host='0.0.0.0',
                port=8000,
                reload=True)
