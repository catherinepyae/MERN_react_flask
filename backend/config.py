import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
CORS(app) #to disable block error for us

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///mydatabase.db"#specifying the location of the local sql lite database. so will be storing on our machine.note: sqlite database is easy to work with flask. 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #will not track all the modification which we make to the database.

db = SQLAlchemy(app)
#creating the instance of the database which give us access to the database which we specified above
#so can create, modify, delete etc. This db object is from "flask_sqlalchemy". 
#what it access is an ORM (object relational mapping), meaning we can have a normal python code, like modification to db and the it will tranform into sql and apply it into the database
