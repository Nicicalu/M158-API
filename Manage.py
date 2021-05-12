import os
import unittest

from flask_script import Manager
from flask_cors import CORS,logging,cross_origin
from app import blueprint

from app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
CORS(app)
logging.getLogger('flask_cors').level = logging.DEBUG
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run(debug=False)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='Test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
    #app.run(debug=False)