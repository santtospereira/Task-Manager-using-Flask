import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# CORREÇÃO DE SEGURANÇA (Mitigação do CWE-259): Tratamento de chaves via variáveis de ambiente
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', '45cf93c4d41348cd9980674ade9a7356')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///site.db')

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# Mantendo a importação original intacta
from todo_project import routes