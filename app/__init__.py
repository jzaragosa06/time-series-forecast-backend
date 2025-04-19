from flask import Flask
from .routes import register_routes
def create_app(): 
    app = Flask(__name__)
    
    #load configuration
    app.config.from_object("app.config.Config")
    
    #register blueprints
    register_routes(app=app)
    
    return app