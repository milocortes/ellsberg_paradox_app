from app import app,db
from flask import request,render_template, flash, redirect, url_for,g
from .models import User, RegistrationForm, LoginForm, ContainerForm,GameOneRound,GameOneSelection,GameOneScore
from flask_login import current_user, login_user, logout_user,login_required
from app import login_manager
import random

import re

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

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def get_current_user():
    g.user = current_user

@app.route('/')
@app.route('/home',methods=["GET","POST"])
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    #if current_user.is_appenticated:
    #    flash('Your are already logged in.', 'info')
    #    return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash(
                'This username has been already taken. Try another one.',
                'warning'
            )
            return render_template('register.html', form=form)
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered. Please login.', 'success')
        return redirect(url_for('login'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    #if current_user.is_appenticated:
    #    flash('You are already logged in.', 'info')
    #    return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = User.query.filter_by(username=username).first()

        if not (existing_user and existing_user.check_password(password)):
            flash('Invalid username or password. Please try again.', 'danger')
            return render_template('login.html', form=form)

        login_user(existing_user)
        flash('You have successfully logged in.', 'success')
        return redirect(url_for('inicio'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

# Esta función acepta las solicitudes web
@app.route('/inicio',methods=["GET","POST"])
def inicio():
    contenedores_nombres = {'containerOne':1,'containerTwo':2,'containerThree':3,'containerFour':4,'containerFive':5,'containerSix':6}
    bolitas_nombres = {1:"Red",2:"Blue",3:"Green"}

    if request.method == "POST":
        form = ContainerForm(request.form)
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
        print("El usuario actual es {}".format(current_user.username))

        ### Generamos los insert
        # Ronda actual
        ronda_actual = GameOneRound.query.filter_by(username=current_user.username).count()
        ronda_actual += 1
        ronda_actual_insert = GameOneRound(current_user.username, ronda_actual)
        db.session.add(ronda_actual_insert)
        db.session.commit()

        # Seleccion del juego
        for contenedor in contenedores:
            name_container = contenedores_nombres[contenedor.name]
            contenedor_insert = GameOneSelection(current_user.username,ronda_actual,name_container,contenedor.data)
            db.session.add(contenedor_insert)
            db.session.commit()

        # Resultado del contenedor seleccionado
        name_container_score = rand_contenedor.name
        bola_elegida_score = int(rand_contenedor.data)
        print("#######################")
        print(current_user.username)
        print(ronda_actual)
        print(name_container_score)
        print(bola_elegida_score)
        print(recompensa)
        
        contenedor_score_insert = GameOneScore(current_user.username,
                                    ronda_actual,
                                    name_container_score,
                                    bola_elegida_score,
                                    recompensa)

        db.session.add(contenedor_score_insert)
        db.session.commit()

        return render_template('index.html', contenedor_random=contenedor_random , bolita_elegida = bolita_elegida,bolita_random=bolita_random , recompensa=recompensa)

    return render_template('index.html')
