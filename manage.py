#!/usr/bin/env python
import os
from  src.app import create_app, db
from src.models.User import User
from src.models.Role import Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_login import login_required


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()