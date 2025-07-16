from .system_info_route import system_info_bp
from .forecast_route import forecast_bp
from .preprocessing_route import preprocess_bp
from .ai_route import ai_bp
from .documentation_route import documentation_bp

def register_routes(app):
    # app.register_blueprint(system_info_bp, url_prefix="/api/system-info")
    # app.register_blueprint(forecast_bp, url_prefix="/api/forecast")
    # app.register_blueprint(clean_bp, url_prefix="/api/clean")
    app.register_blueprint(documentation_bp, url_prefix="/")
    app.register_blueprint(ai_bp, url_prefix="/api/ai")
    app.register_blueprint(system_info_bp, url_prefix="/api/system-info")
    app.register_blueprint(forecast_bp, url_prefix="/api/forecast")
    app.register_blueprint(preprocess_bp, url_prefix="/api/preprocess")