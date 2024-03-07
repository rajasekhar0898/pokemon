from flask import Flask
from pokemon.extensions.db import db

# Create an instance of SQLAlchemy

def load_config(app):
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = ("mysql+pymysql://avnadmin:AVNS_dro4YtU_Jx8pbFN0OOc@mysql-class-rajasekharvadlamudi57-d7cd.a.aivencloud.com:12873/defaultdb")

def register_blueprints(app):
    from pokemon.routes import main, auth, poker

    app.register_blueprint(main.main_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(poker.poker_bp)

def create_app():
    server = Flask(__name__)
   
    load_config(server)

    register_blueprints(server)
    
    # Initialize SQLAlchemy with the Flask app
    db.init_app(server)

    with server.app_context():
        db.create_all()
    return server
