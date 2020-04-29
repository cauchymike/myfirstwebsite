#this is the __init__.py file under myproject folder
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

#we are regeistering our blueprints after we define our db inorder for blueprints to work
from myproject.puppies.views import students_blueprint
from myproject.owners.views import parent_blueprint

app.register_blueprint(parent_blueprint, url_prefix='/parent')
app.register_blueprint(students_blueprint,url_prefix='/students')
