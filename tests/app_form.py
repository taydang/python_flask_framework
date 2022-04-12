from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, request, make_response, abort, render_template, session, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class LoginForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
@app.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        # name = loginForm.name.data
        # loginForm.name.data = ''
        session['name'] = loginForm.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=loginForm, name=session.get('name'))

if __name__ == '__main__':
    manager.run()