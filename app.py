from db_functions import db_connect, db_insert_user, db_find_all, db_delete_one
from db_functions import MONGO_URI
from forms import BuyForm, LoginForm
from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__, template_folder = 'templates')

inventario = db_connect(MONGO_URI, 'Nombre_del_Proyecto', 'Nombre_de_las_colecciones')
usuarios = db_connect(MONGO_URI, 'Nombre_del_Proyecto', 'Nombre_de_las_colecciones')

app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = BuyForm(request.form)

    if 'user' in session:
        session_flag = True
    else:
        session_flag = False
    
    if request.method == 'POST':
        item = form.item.data
        precio = form.precio.data

        if request.form['submit_button'] == 'Salir':
            session.pop('user', None)
            return redirect('/')
        if request.form['submit_button'] == 'Borrar':
            if item != None and precio != None:
                coso = {
                    'item': item,
                    'precio': precio
                }
                db_delete_one(inventario, coso)
        else:
            if item != None and precio != None:
                coso = {
                    "item": item,
                    "precio": precio
                }
                db_insert_user(inventario, coso)

    items = db_find_all(inventario)
            
    return render_template('admin.html', items=items, session_flag=session_flag)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    error = False

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        print(username)
        print(password)

        if username != None and password != None:
            usuario = {
                'username': username,
                'password': password
            }

            trying = db_find_all(usuarios, usuario)

            try:
                for tried in trying:
                    tried['username']
                    session['user'] = username
                    return redirect('/')
            finally:
                error = True

    return render_template('login.html', error = error)

if __name__ == '__main__':
	app.run(debug=True, port=8000)