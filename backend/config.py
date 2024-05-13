from flask import flask
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) #to disable block error for us

app.config["SQLALCHEMY_DATABASE_URL"]= "sqlite://mydatabase.db"