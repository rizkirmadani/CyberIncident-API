from app.routes.user_routes import bp as users_bp
from app.routes.asset_routes import bp as assets_bp
from app.routes.category_routes import bp as categories_bp
from app.routes.incident_routes import bp as incidents_bp

def register_routes(app):
    app.register_blueprint(users_bp, url_prefix='/api/v1/users')
    app.register_blueprint(assets_bp, url_prefix='/api/v1/assets')
    app.register_blueprint(categories_bp, url_prefix='/api/v1/categories')
    app.register_blueprint(incidents_bp, url_prefix='/api/v1/incidents')
