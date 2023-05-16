from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main.views import main_bp
    app.register_blueprint(main_bp)

    from app.auth.views import auth_bp
    app.register_blueprint(auth_bp)
    
    return app