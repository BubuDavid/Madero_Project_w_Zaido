from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class BuyForm(Form):
    item = StringField('item', validators=[DataRequired()])
    precio = IntegerField('precio', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
