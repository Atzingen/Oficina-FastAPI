from fastapi import FastAPI, Response, status
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

@app.get("/")
def home():
    return "home sweet home !!!"

if __name__ == '__main__':
    uvicorn.run('main:app')
                # reload=True
                # port=8000
                # host='0.0.0.0'