# Oficina-FastAPI

Código utilizado na oficina sobre criação de API's para sensores e IoT utilziando FastAPI

As dependências de todos os exemplos podem ser instaladas com o arquivo requirements.txt

```bash
pip install -r requirements.txt
```

Cada exemplo está em uma pasta e dece ser executado de forma isolada de dentro da pasta específica.

```bash
cd 01-hello
python main.py
```

# Tópicos:

* 01-Hello
    * O básico de como iniciar um programa com FastAPI e uvicorn
    * Portas, host e como executar via uvcorn e app.run()
    * docs
<br /><br />

* 02-Rotas
    * tópicos e subtópicos em uma rota.
    * Tipos nas rotas via *type hint*
    * Responses
    * curl e POSTMAN
<br /><br />

* 03-Media e outros tipos
    * Tipos de Response
    * Recebendo Imagens e outros arquivos
    * Devolvendo dados
    * Streaming
<br /><br />

* 04-DB
    * CRUD
    * ORM Sqlalchemy
    * Dataclasses
    * Sqlite
<br /><br />

* 05-Jinja
    * templates
    * variáveis dentro do html
    * estruturas de controle
<br /><br />

* 06-Deploy
    * https
    * Certificados
    * Tokens
    * workers
