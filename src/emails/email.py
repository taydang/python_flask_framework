import os
from  src.app import create_app, db
from flask import current_app, render_template
from flask_mail import Message
from ..app import mail
from threading import Thread

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)