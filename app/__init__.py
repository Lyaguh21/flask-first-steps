from flask import Flask
from dotenv import load_dotenv

from .config import Config
from .extensions import db, migrate

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # регистрируем роуты (blueprints)
    from .routes.users import users_bp
    app.register_blueprint(users_bp)
    
    return app
