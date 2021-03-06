from flask import Flask, request, make_response, abort, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index ():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found (e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def interval_server_error (e):
    return render_template('500.html'), 500
    
if __name__ == '__main__':
    manager.run()