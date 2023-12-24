from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes import routes_blueprint

        app.register_blueprint(routes_blueprint)

        return app
