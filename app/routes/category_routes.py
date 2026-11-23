from flask import Blueprint
from app.controllers import category_controller as c

bp = Blueprint('categories', __name__)

bp.add_url_rule('', 'list_categories', c.list_categories, methods=['GET'])
bp.add_url_rule('', 'create_category', c.create_category, methods=['POST'])
bp.add_url_rule('/<int:id>', 'get_category', c.get_category, methods=['GET'])
bp.add_url_rule('/<int:id>', 'update_category', c.update_category, methods=['PUT'])
bp.add_url_rule('/<int:id>', 'delete_category', c.delete_category, methods=['DELETE'])
