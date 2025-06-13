from .system_info_routes import system_info_bp
from .forecast_route import forecast_bp
from .preprocessing_routes import clean_bp
from .ai_routes import ai_bp

def register_routes(app):
    app.register_blueprint(system_info_bp, url_prefix="/system-info")
    app.register_blueprint(forecast_bp, url_prefix="/forecast")
    app.register_blueprint(clean_bp, url_prefix="/clean")
    app.register_blueprint(ai_bp, url_prefix="/ai")