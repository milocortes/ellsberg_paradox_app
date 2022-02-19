# Importamos el objeto app, las funciones de flask  así como las formas y
# modelos de la aplicación
from app import app
import random
from .forms import *
from flask import render_template,jsonify, redirect, url_for, request

# Esta url redirecciona a la URL hola
@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('inicio'))

# Esta función acepta las solicitudes web
@app.route('/inicio',methods=["GET","POST"])
def inicio():
    contenedores_nombres = {'containerOne':1,'containerTwo':2,'containerThree':3,'containerFour':4,'containerFive':5,'containerSix':6}
    bolitas_nombres = {1:"Red",2:"Blue",3:"Green"}

    if request.method == "POST":
        form = LoginForm(request.form)
        print("Contenedor 1: ",form.containerOne.data)
        print("Contenedor 2: ",form.containerTwo.data)
        print("Contenedor 3: ",form.containerThree.data)
        print("Contenedor 4: ",form.containerFour.data)
        print("Contenedor 5: ",form.containerFive.data)
        print("Contenedor 6: ",form.containerSix.data)


        contenedores = [form.containerOne,form.containerTwo,form.containerThree,form.containerFour,form.containerFive,form.containerSix]

        rand_contenedor = random.choice(contenedores)

        print("El contenedor aleatorio {} con valor {}".format(rand_contenedor.name,rand_contenedor.data))

        recompensa,bolita_random = get_bolita_contenedor(rand_contenedor.name,rand_contenedor.data)
        bolita_random = bolitas_nombres[bolita_random]
        contenedor_random=contenedores_nombres[rand_contenedor.name]
        bolita_elegida=bolitas_nombres[int(rand_contenedor.data)]
        print("Contenedor {}".format(contenedor_random))
        print("Bola elegida {}".format(bolita_elegida))

        return render_template('index.html', contenedor_random=contenedor_random , bolita_elegida = bolita_elegida,bolita_random=bolita_random , recompensa=recompensa)

    return render_template('index.html')
