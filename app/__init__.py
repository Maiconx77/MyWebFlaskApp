# app/__init__.py
from flask import Flask

# Cria uma instância do Flask
app = Flask(__name__)

# Importa as rotas
from app import routes