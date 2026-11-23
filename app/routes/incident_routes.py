from flask import Blueprint
from app.controllers import incident_controller as c

bp = Blueprint('incidents', __name__)

bp.add_url_rule('', 'list_incidents', c.list_incidents, methods=['GET'])
bp.add_url_rule('', 'create_incident', c.create_incident, methods=['POST'])
bp.add_url_rule('/<int:id>', 'get_incident', c.get_incident, methods=['GET'])
bp.add_url_rule('/<int:id>', 'update_incident', c.update_incident, methods=['PUT'])
bp.add_url_rule('/<int:id>', 'delete_incident', c.delete_incident, methods=['DELETE'])
bp.add_url_rule('/<int:id>/updates', 'add_update', c.add_update, methods=['POST'])
bp.add_url_rule('/<int:id>/updates', 'list_updates', c.list_updates, methods=['GET'])
