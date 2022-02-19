from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, widgets, TextAreaField, SelectMultipleField
from wtforms.validators import InputRequired, EqualTo
from wtforms.fields import TelField,DateField
import random

import re

class LoginForm(FlaskForm):
    containerOne = StringField('containerOne', [InputRequired()])
    containerTwo = StringField('containerTwo', [InputRequired()])
    containerThree = StringField('containerThree', [InputRequired()])
    containerFour = StringField('containerFour', [InputRequired()])
    containerFive = StringField('containerFive', [InputRequired()])
    containerSix = StringField('containerSix', [InputRequired()])

def get_bolita_contenedor(contenedor,valor):

    bolas_total = 36

    valor_rojas_contenedores = {'containerOne':9,'containerTwo':10,'containerThree':11,'containerFour':12,'containerFive':13,'containerSix':14}

    R = valor_rojas_contenedores[contenedor]
    restantes = bolas_total - R
    B = int(restantes * random.random())
    G = bolas_total - R - B

    lista_bolas = [1 for i in range(R)] + [2 for i in range(B)] + [3 for i in range(G)]

    random.shuffle(lista_bolas)

    select_random = random.choice(lista_bolas)

    print("La bola sacada al asar es {} y la elegida por el usuario es {}".format(select_random,valor))

    if int(select_random)==int(valor):
        return 10,select_random
    else:
        return 0,select_random
