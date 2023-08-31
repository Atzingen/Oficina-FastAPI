from typing import List
from fastapi import FastAPI, Response, status
import uvicorn

app = FastAPI(
    title=" Exemplo FASTAPI - IOT",
    version="1.0.0",
    description=''''
        exemplo FASTAPI - IOT
        
        Neste exemplo vamos criar uma API para receber dados de sensores
    '''
)

@app.get("/")
def home():
    return "home sweet home !!!"

@app.post('/insert_sensor_data')
def insert_sensor_data(sensor_id: int,
                       sensor_values: List[float]):
    print(sensor_id, sensor_values)
    return status.HTTP_201_CREATED

@app.get('/read_sensor_data')
def read_sensor_data(sensor_id: int,
                qt: int = 1):
    print(sensor_id)
    return 'OK'

if __name__ == '__main__':
    uvicorn.run('main2:app', 
                host='0.0.0.0',
                port=8000,
                reload=True)