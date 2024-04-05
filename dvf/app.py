from flask import Flask
from os import environ as env

from endpoints.vulnerable_routes import vulnerable
from endpoints.secure_routes import secure
from db import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{env["DB_USER"]}:{env["PASSWORD"]}@{env["HOST"]}:{env["PORT"]}/{env["DATABASE"]}'

db = init_db(app)

app.register_blueprint(vulnerable)
app.register_blueprint(secure)