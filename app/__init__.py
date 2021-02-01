from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # Starts tge flask program??
app.config.from_object(Config)# Tells the app Cobnfig exists
db=SQLAlchemy(app) #initializes the database
migrate= Migrate(app,db) #initializes the migration engine
from app import routes, models #models defines the sturcture of the database
#if __name__=="__main__":
#    app.run(debug=True)