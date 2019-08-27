"""
Entrypoint of the application.

Manager and Migrate are set up and the blueprint for app
is created.

"""

import os
import unittest
from logging import getLogger

from flask import current_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.logging_config import setup_logger
from app.main.models import users

setup_logger()
LOG = getLogger(__name__)

app = create_app(os.getenv('FLASK_ENV') or 'dev')

app.register_blueprint(blueprint)
LOG.info('blueprints registered')

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    """Run the flask app."""
    LOG.info('initiating app...')
    app.run(host=current_app.config['HOST'],
            port=current_app.config['PORT'], debug=current_app.config['DEBUG'])


@manager.command
def test():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        # Return error code
        return 0
    return 1


@manager.command
def rollback():
    """Roll back database to a previous state in case of exception."""
    db.session.rollback()
    LOG.warning('Last session rolled back!')

if __name__ == '__main__':
    manager.run()
