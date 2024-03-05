from config.flask import *
from routes.healthy import healthy_routes
from config.db.connection import db_connection

# Criando a aplicação
app = create_app()

# Fazendo a conexão com o banco de dados
db = db_connection(app)

# Mapeando as rotas
healthy_routes(app)

# Rodando a aplicação
run_app()

