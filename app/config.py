import os

class Config: 
    DEBUG = False
    TESTING = False
    
    PORT = os.environ.get("PORT", 5000)
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc123")
    