from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from .routes import register_routes
def create_app(): 
    app = Flask(__name__)
    
    #load configuration
    app.config.from_object("app.config.Config")
    
    #env
    load_dotenv() 
    
    #enable cors for frontend
    CORS(app, origins=["http://localhost:5173"])
    
    #register blueprints
    register_routes(app=app)
    
    return app