from db_functions import db_connect, db_insert_user, db_find_all, db_delete_one
from db_functions import MONGO_URI
from forms import BuyForm, LoginForm
from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'templates')

users = db_connect(MONGO_URI, 'Project_name', 'Collection_Name')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = BuyForm(request.form)
    items = db_find_all(users)
    
    if request.method == 'POST':
        item = form.item.data
        precio = form.precio.data
        if item != None and precio != None:
            coso = {
                "item": item,
                "precio": precio
            }
            db_insert_user(users, coso)
            items = db_find_all(users)
            
    return render_template('admin.html', items=items)

if __name__ == '__main__':
	app.run(debug=True)