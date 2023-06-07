#app.py: This is the entry point of your application where you initialize your Flask application.

from flask import Flask
from app.routes.example_route import example_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(example_blueprint)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
