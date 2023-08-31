from fastapi import FastAPI, Response, status
import uvicorn
import random

nerd_physics_jokes = [
    "Por que os físicos não fazem a barba? Porque querem evitar os cortes quânticos!",
    "O que o físico disse para a partícula carregada que estava na cadeia? Mantenha-se positiva!",
    "Por que os físicos nunca jogam futebol? Porque eles sempre quebram as leis da física!",
    "Por que a mecânica quântica não faz nenhum sentido? Porque até as partículas não sabem onde estão!",
    "Por que um gato vivo e um gato morto foram para uma festa juntos? Porque eles eram gatos de Schrödinger!",
    "Por que os físicos são péssimos cozinheiros? Porque sempre usam a energia no lugar errado!",
    "Por que os físicos adoram o inverno? Porque eles adoram quando as coisas atingem o zero absoluto!",
    "Como um físico de partículas adota um cachorro? Primeiro, ele procura um bom condensado de Bose-Einstein!",
    "O que um físico disse ao chegar atrasado para a reunião? Desculpe, eu fui relativamente lento!",
    "Qual o prato preferido de um físico? Um 'quark-e'joada!"
]

app = FastAPI()

@app.get("/")
def home():
    return "Lar doce lar !!!"

@app.post("/insert_image/")
def insert_image(img: bytes):
    print(img)
    return status.HTTP_201_CREATED

@app.get("/sensor/")
def sensor(valor: int,
           id_sensor: int):
    print(valor)
    return f'https://http.cat/status/{status.HTTP_422_UNPROCESSABLE_ENTITY}'

@app.get("/piadas/")
def piadas():
    # qt_piadas = len(nerd_physics_jokes)
    return random.choice(nerd_physics_jokes)

if __name__ == '__main__':
    uvicorn.run('main3:app', 
                host='0.0.0.0',
                reload=True)

