from flask import Flask, request, make_response, abort
from flask_script import Manager
app = Flask(__name__)

@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/user-agent')
def userAgent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

# abort function, which is used for errorhandling.
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

# @app.route('/make-response')
# \
    # 4def makeResponse():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response

manager = Manager(app)
if __name__ == '__main__':
    manager.run()

# if __name__ == '__main__':
#     app.run(debug=True)