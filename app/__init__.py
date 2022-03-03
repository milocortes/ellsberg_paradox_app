from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

conn_string = 'postgresql://ellsberg_user:ellsberg_user@localhost:5432/ellsberg_db'
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
app.config['SECRET_KEY'] = "SECRET_KEY"

db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from app import views

db.create_all()
