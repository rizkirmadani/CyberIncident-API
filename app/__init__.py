from flask import Flask, jsonify
from app.extensions import db, migrate
from config import Config
from app.models import User, Asset, IncidentCategory, Incident, IncidentUpdate
from app.routes import register_routes

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    migrate.init_app(app, db)
    register_routes(app)

    @app.get('/api/v1/health')
    def health():
        return jsonify({'success': True, 'message': 'CyberIncident API is running', 'version': '1.0'}), 200


    @app.errorhandler(404)
    def not_found(_):
        return jsonify({'success':False,'error':{'code':'NOT_FOUND','message':'Endpoint atau data tidak ditemukan'}}),404


    @app.errorhandler(500)
    def internal_error(_):
        db.session.rollback()
        return jsonify({'success':False,'error':{'code':'INTERNAL_SERVER_ERROR','message':'Terjadi kesalahan pada server'}}),500
    return app
