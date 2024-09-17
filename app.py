from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from config import Config
from models import db, User
from routes.auth import auth_blueprint
from routes.tasks import tasks_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(tasks_blueprint, url_prefix='/tasks')

    @app.route('/')
    def home():
        if current_user.is_authenticated:
            return redirect(url_for('tasks.dashboard'))
        return redirect(url_for('auth.login'))
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)
