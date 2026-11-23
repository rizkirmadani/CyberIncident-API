from flask import Blueprint
from app.controllers import user_controller as c

bp = Blueprint('users', __name__)

bp.add_url_rule('', 'list_users', c.list_users, methods=['GET'])
bp.add_url_rule('', 'create_user', c.create_user, methods=['POST'])
bp.add_url_rule('/<int:id>', 'get_user', c.get_user, methods=['GET'])
bp.add_url_rule('/<int:id>', 'update_user', c.update_user, methods=['PUT'])
bp.add_url_rule('/<int:id>', 'delete_user', c.delete_user, methods=['DELETE'])
