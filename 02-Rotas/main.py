from fastapi import FastAPI, Response, status
from typing import List
import random
import uvicorn

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

@app.get("/read_sensor/")
def read_sensor(sensor_id: int = 1, qt: int = 1):
    sensor_data = [random.random() for _ in range(qt)]
    return {f'sensor_{sensor_id}': sensor_data}

@app.post("/insert_sensor")
def insert_sensor_post(numbers: List[int]):
    print(numbers)
    return status.HTTP_202_ACCEPTED

@app.get("/insert_sensor/{sensor_id}/{sensor_value}")
def insert_sensor(sensor_id: int, 
           sensor_value: float,
           response: Response):
    print(sensor_id, sensor_value)
    if sensor_id > 0 and sensor_id < 10:
        response.status_code = status.HTTP_202_ACCEPTED
    else:
        response.status_code = status.HTTP_403_FORBIDDEN
    return response

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)