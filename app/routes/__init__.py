from .system_info_routes import system_info_bp

def register_routes(app):
    app.register_blueprint(system_info_bp, url_prefix="/system-info")