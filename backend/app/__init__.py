from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
# Order is important here. Marshmallow needs to be initialized after SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from app import routes, car_model, model, schemas
