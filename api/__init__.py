from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import pymysql
from flask_jwt_extended import JWTManager

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)

# configurações pra chave secreta do JWT
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

from .views import curso_views, formacao_views, professor_views, usuario_views, login_views, refresh_token_views
from .models import curso_model, formacao_model, professor_model, usuario_model
