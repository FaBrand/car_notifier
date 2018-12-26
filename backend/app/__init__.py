from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, car_model, model
