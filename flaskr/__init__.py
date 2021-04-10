# export FLASK_APP=flaskr
# export FLASK_ENV=development
# export APP_SETTINGS="flaskr.config.DevelopmentConfig"
import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(os.environ['APP_SETTINGS'])

    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app