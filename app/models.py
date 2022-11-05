from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    pwdhash = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class GameOneRound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)

    def __init__(self, username,round):
        self.username = username
        self.round = round

class GameOneSelection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)
    containername = db.Column(db.String(20))
    bet = db.Column(db.Integer)

    def __init__(self, username,round,containername,bet):
        self.username = username
        self.round = round
        self.containername = containername
        self.bet = bet

class GameOneScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)
    containername = db.Column(db.String(20))
    bet = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, username,round,containername,bet,score):
        self.username = username
        self.round = round
        self.containername = containername
        self.bet = bet
        self.score = score

class GameTwoRound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)

    def __init__(self, username,round):
        self.username = username
        self.round = round

class GameTwoSelection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)
    containername = db.Column(db.String(20))
    bet = db.Column(db.Integer)

    def __init__(self, username,round,containername,bet):
        self.username = username
        self.round = round
        self.containername = containername
        self.bet = bet

class GameTwoScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)
    containername = db.Column(db.String(20))
    bet = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, username,round,containername,bet,score):
        self.username = username
        self.round = round
        self.containername = containername
        self.bet = bet
        self.score = score

######

class GameThreeRound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)

    def __init__(self, username,round):
        self.username = username
        self.round = round

class GameThreeSelection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)
    containername = db.Column(db.String(20))
    bet = db.Column(db.Integer)

    def __init__(self, username,round,containername,bet):
        self.username = username
        self.round = round
        self.containername = containername
        self.bet = bet

class GameThreeScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    round = db.Column(db.Integer)
    containername = db.Column(db.String(20))
    bet = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, username,round,containername,bet,score):
        self.username = username
        self.round = round
        self.containername = containername
        self.bet = bet
        self.score = score

class RegistrationForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = PasswordField(
        'Password', [
            InputRequired(), EqualTo('confirm', message='Passwords must match')
        ]
    )
    confirm = PasswordField('Confirm Password', [InputRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])

class ContainerForm(FlaskForm):
    containerOne = StringField('containerOne', [InputRequired()])
    containerTwo = StringField('containerTwo', [InputRequired()])
    containerThree = StringField('containerThree', [InputRequired()])
    containerFour = StringField('containerFour', [InputRequired()])
    containerFive = StringField('containerFive', [InputRequired()])
    containerSix = StringField('containerSix', [InputRequired()])
