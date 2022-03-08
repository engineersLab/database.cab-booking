from flask import Flask
from flask_migrate import Migrate
from service.models import *
from service.db import db
from configparser import ConfigParser

app = Flask(__name__)

config = ConfigParser()
config.read("config.ini")
db_creds = config["database"]

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{db_creds['USERNAME']}:{db_creds['PASSWORD']}@{db_creds['HOST']}:{db_creds['PORT']}/cab-booking"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)
app.db = db
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)